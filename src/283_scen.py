#How do I perform secondary sorting in python?


There is no built-in function in Python for secondary sorting, but the sorted() function accepts a key function that can be used to sort by multiple criteria.

def sort_by_last_and_first_name(s):
    return s[1], s[0]

sorted(names, key=sort_by_last_and_first_name)