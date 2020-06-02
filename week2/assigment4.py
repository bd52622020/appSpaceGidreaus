
###Q1
def count_lower_upper_letters(strng):
    lower_count = sum(1 for char in strng if char.islower())
    upper_count = sum(1 for char in strng if char.isupper())
    return lower_count, upper_count

print("Q1")

print("Hello world (lower letters, upper letters)", count_lower_upper_letters("Hello world"))
print("Hello */.. world! (lower letters, upper letters)", count_lower_upper_letters("Hello */.. world!"))

###Q1

print("Q2")

def print_pasckal_trangle(rows):
    line = []
    for i in range(0, rows):
        new_line = [1]
        if i > 1:
            for j in range(i-1):
                new_line.append(sum(line[j:j+2]))
        if i > 0:
            new_line.append(1)
        line = new_line
        [print(e, end=" ") for e in line]
        print("")
        
       
print_pasckal_trangle(8)

