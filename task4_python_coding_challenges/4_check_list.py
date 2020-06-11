def check_list(num_list):
    if num_list[0] == num_list[-1]:
        return True
    else:
        return False

print("Q4")     
print("[1,2]:", check_list([1,2]))
print("[3]:", check_list([3]))
print("[3,5,3]:", check_list([3,4,3]))     
