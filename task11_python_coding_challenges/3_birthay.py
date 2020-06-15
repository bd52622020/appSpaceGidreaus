import json

if __name__ == '__main__':
    name = input("Please enter a name:\n")
    
    with open('names.json') as json_file:
        my_dict = json.load(json_file)
        
        
    if name in my_dict.keys():
        print(name, "birthay:", my_dict[name])
    else:
        print("There isn't", name, "in the file.")
        