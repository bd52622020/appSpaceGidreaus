import operator

def get_sorted_list(x):
    return [a[1] for a in sorted(x.items(), key = operator.itemgetter(1))]

stud_dict = {"B_student":"B_name", "A_student":"A_name", "L_student":"L_name","W_student":"W_name", "C_student":"C_name"}

print("Dictonary:", stud_dict)
print("Sorted values:", get_sorted_list(stud_dict))