
if __name__ == '__main__':
    filter_divisible = lambda x: (x % 13 == 0) | (x % 19 == 0)
    my_list = [13,15,18,19,39,54]
    result = list(filter(filter_divisible, my_list))
    print(my_list, " filtered by lamda function:", result)
