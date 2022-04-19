#How do I sum the first value in each tuple in a list of tuples in Python?


def sum_first_value(lst): 

total = 0

for t in lst: 

total += t[0]

return total