import os

def read_file(file_path):
    try:
        if os.path.exists(file_path):
                with open(file_path) as f:
                        head = [next(f) for x in range(10)]
                print(head)
        else:
                print("File does not exist.")
    except:
        print("An exception occured")
    finally:
        print("Code finished")

file_path = os.path.join("..","notes.txt")
read_file(file_path)
