def count_lower_upper_letters(strng):
    lower_count = sum(1 for char in strng if char.islower())
    upper_count = sum(1 for char in strng if char.isupper())
    return lower_count, upper_count

print("Hello world (lower letters, upper letters)", count_lower_upper_letters("Hello world"))
print("Hello */.. world! (lower letters, upper letters)", count_lower_upper_letters("Hello */.. world!"))