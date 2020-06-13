from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from datetime import datetime
import subprocess


#U_ITEM_PATH =  "/home/maria_dev/u.item2"  #"hdfs:///user/maria_dev/data/u.item2"
U_ITEM_PATH = "hdfs://sandbox-hdp.hortonworks.com:8020/user/maria_dev/data/u.item2"
U_DATA_PATH = "hdfs://sandbox-hdp.hortonworks.com:8020/user/maria_dev/data/u.data"

ratings_columns = ["user id", "item id", "rating", "timestamp"]  
user_columns = ["user id", "age","gender", "occupation", "zip code"]
movies_columns =  ['movie id', 'movie title', 'release date', 'video release date', 'IMDb URL', 'unknown', 'Action', 'Adventure', 'Animation', "Children's", 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']

# This function just creates a Python "dictionary" we can later
# use to convert movie ID's to movie names while printing out
# the final results.
def load_movie_names(file_name):
    movieNames = {}
    with open(file_name) as f:
        for line in f:
            fields = line.split('|')
            movieNames[int(fields[0])] = fields[1]
    return movieNames
    
def load_ratings_5(file_name):
    movie_ids = []
    cat = subprocess.Popen(["hadoop", "fs", "-cat", file_name], stdout=subprocess.PIPE)
    for line in cat.stdout:
        fields = line.split('\t')
        rating = int(fields[2])
        if rating == 5:
            movie_ids.append(fields[1])
    return list(set(movie_ids))
    
# Read files as stream from hdfs
def load_movie_names_2(file_name):
    movie_names = {}
    cat = subprocess.Popen(["hadoop", "fs", "-cat", file_name], stdout=subprocess.PIPE)
    for line in cat.stdout:
        fields = line.split('|')
        movie_names[int(fields[0])] = fields[1]
    return movie_names

# Take each line of u.data and convert it to (movieID, (rating, 1.0))
# This way we can then add up all the ratings for each movie, and
# the total number of ratings for each movie (which lets us compute the average)
def parseInput(line):
    fields = line.split()
    return (int(fields[1]), (float(fields[2]), 1.0))

def parse_input_1(line):
    fields = line.split()
    return (int(fields[1]),  1.0)
        
def parse_input_3(line):
    fields = line.split("|")
    if fields[2] == "":
        field2 = None
    else:
        field2 = datetime.strptime(fields[2], '%d-%b-%Y')
    return (fields[0],  fields[1], field2)
    
def parse_input_4(line):
    fields = line.split("|")
    return (fields[0],  fields[3])
    
def parse_input_5(line):
    fields = line.split("\t")
    return (fields[1],  datetime.fromtimestamp(float(fields[3])))
     

def df_column_sum(df, col):
    return (col, df.select(col).rdd.map(lambda x: (1,int(x[0]))).reduceByKey(lambda x,y: x + y).collect()[0][1])
    
def get_genres_sums(df, cols):

    results = []
    for col in cols:
        results.append(df_column_sum(df, col))
    return results

def get_movie_genres(cols, columns_names):
    genres = []
    for i in range(len(cols)):
        if cols[i] == "1":
            genres.append(columns_names[i])
    return ", ".join(genres)
    
if __name__ == "__main__":
    # The main script - create our SparkContext
    conf = SparkConf().setAppName("WorstMovies")
    sc = SparkContext(conf = conf)
    spark = SparkSession(sc)
    #sc.setLogLevel("WARN")
    
    # Load data
    ratings = sc.textFile("/user/maria_dev/data/u.data")
    users = sc.textFile("/user/maria_dev/data/u.user")
    movies = sc.textFile("/user/maria_dev/data/u.item2") # file is converted into UTF8 encoding
    
    # Define data frames
    ratings_df = ratings.map(lambda k: k.split("\t")).toDF(ratings_columns)
    movies_df = movies.map(lambda k: k.split("|")).toDF(movies_columns)
    users_df = users.map(lambda k: k.split("|")).toDF(user_columns)
    merged_df = ratings_df.join(movies_df, ratings_df["item id"] == movies_df["movie id"], how = "left").drop("movie id")
    movie_names = load_movie_names_2(U_ITEM_PATH)
    
    
    ### Q1& Q2) Print a list of the 10 movies that received the most number of ratings, sorted by the number of ratings.
    movies_counts = ratings.map(parse_input_1).reduceByKey(lambda x1, x2: x1 + x2).sortBy(lambda x: x[1], ascending=False).take(10)
    results_1 = [ (r[0], r[1], movie_names[r[0]]) for r in movies_counts] # (movie id, movie count, movie title)
     
    ### Q3) Print a list of the number of ratings received by each genre.
    results_3 = get_genres_sums(merged_df, movies_columns[5:])
    
    ### Q4) Print the oldest movie with a 5 rating.
    movies_ids = load_ratings_5(U_DATA_PATH)
    movies_df2 = movies.map(parse_input_3).toDF(['movie id', 'movie title', 'release date'])
    ind_filter = (movies_df2["movie id"].isin(movies_ids)) & (~movies_df2['release date'].isNull()) 
    results_4 =  movies_df2.filter(ind_filter).sort(movies_df2["release date"] , ascending=True).take(1)
    
    ### Q5 Print a list of the genre of the top 10 most rated movies.
    top_rated_movie_ids = [str(r[0]) for r in results_1]
    top_rated_movies_df = movies_df.filter(movies_df["movie id"].isin(top_rated_movie_ids))
    genres_cols = movies_columns[5:]
    top_rated_movies_genres = top_rated_movies_df.select(genres_cols).rdd.map(lambda row: get_movie_genres(row, genres_cols)).collect()
    ids = [id["movie id"] for id in top_rated_movies_df.select(["movie id"]).collect()]
    results_5 = [(r[2], top_rated_movies_genres[ids.index(str(r[0]))]) for r in results_1] #(movie title, genres)
    
    ### Q6 Print the title of the movie that was rated the most by students
    students_id = users.map(parse_input_4).filter(lambda cols: cols[1] == "student").map(lambda col : col[0]).collect()
    students_df = ratings_df.select(["user id", "item id"]).filter(ratings_df["user id"].isin(students_id))
    students_counts = students_df.rdd.map(lambda row: (row[1], 1)).reduceByKey(lambda x1, x2: x1 + x2).sortBy(lambda x: x[1], ascending=False).take(1)[0]
    
    ### Q7 Print the list of movies that received the highest number of 5 rating
    rating_5_df = merged_df.select(["item id","rating"]).filter(merged_df["rating"] == 5)
    results_7 = rating_5_df.rdd.map(lambda row: (row[0], 1)).reduceByKey(lambda x1, x2: x1 + x2).sortBy(lambda x: x[1], ascending=False).take(10)
    
    ### Q8 Print the list of zip codes corresponding to the highest number of users that rated movies.
    results_8 = users_df.select('zip code').groupBy('zip code').count().orderBy('count', ascending=False).take(10)
    
    ### Q9 Find the most rated movie by users in the age group 20 to 25.
    user_25_30_ids =  [ id["user id"] for id in  users_df.select('user id', 'age').filter(users_df["age"].between(20, 25)).select('user id').collect()]
    movies_id = ratings_df.select(["user id", "item id"]).filter(ratings_df["user id"].isin(user_25_30_ids)).select("item id").groupBy('item id').count().orderBy('count', ascending=False).select("item id").take(1)[0]["item id"]
    results_9 = movies_df.select('movie id', 'movie title').filter(movies_df["movie id"] == movies_id).select('movie title').take(10)[0]
    
    ### Q10 Print the list of movies that were rate after year 1960.
    ratings_df2 = ratings.map(parse_input_5).toDF(["item id", "date"])
    movies_ids = [ id["item id"] for id in ratings_df2.filter(ratings_df2["date"] > datetime(1960,12,31)).select("item id").collect()]
    results_10 = movies_df.select(["movie id", "movie title"]).filter(movies_df["movie id"].isin(movies_ids)).take(10)
    
    
    ### Results print
    print "### Q1, Q2 ###"
    print '==================================================='
    for r in results_1:
        print "{:30} counts : {}".format(r[2], r[1])
    print "\n### Q3 ###"
    print '==================================================='
    for r in results_3:
        print "{:13}: {}".format(r[0], r[1])
    print "\n### Q4 ###"
    print '==================================================='
    print results_4[0][1]
    print "\n### Q5 ###"
    print '==================================================='
    for r in results_5:
        print "{:30} genres : {}".format(r[0], r[1])
    print "\n### Q6 ###"
    print '==================================================='
    print movie_names[int(students_counts[0])]
    print "\n### Q7 ###"
    print '==================================================='
    print 'First 10 movies with the highest number of 5 rating'
    for r in results_7:
        print "{:32}: {}".format(movie_names[int(r[0])], r[1])
    print "\n### Q8 ###"
    print '==================================================='
    for r in results_8:
        print "zipcode: {:6}  - {}".format(r[0], r[1])
    print "\n### Q9 ###"
    print '==================================================='
    print results_9["movie title"]
    print "\n### Q10 ###"
    print '==================================================='
    print 'First ten movies which rate after year 1960 (all movies rated after 1960):'
    for r in results_10:
        print(r[1])
    