#How do I sort a list of dictionaries by values of the dictionary in Python?


Here is one way to do it:

mylist = [{'name':'bob','age':21}, {'name':'jane','age':17}, {'name':'john','age':19}]

mylist.sort(key=lambda d: d['age'])

for d in mylist:
    print d['name'], d['age']