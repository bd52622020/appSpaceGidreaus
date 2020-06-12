def consecutive_duplicate(list1):
    new_list = []
    a = None
    for el in list1:
        if el != a:
            new_list.append(el)
        a = el
    return new_list
    



if __name__ == '__main__':
    a = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
    print("List ", a, "removing consecutive duplicates:", consecutive_duplicate(a))