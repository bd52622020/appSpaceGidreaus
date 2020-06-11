def is_key_exists(key, dict_):
    if key in dict_.keys():
        print("Key", key, "exists in a given dictionary.")
    else:
        print("Key", key, "doesn't exist in a given dictionary.")

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

is_key_exists(5, d)
is_key_exists(10, d)
