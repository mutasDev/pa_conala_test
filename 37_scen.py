#python save list `mylist` to file object 'save.txt'


mylist = [1, 2, 3, 4, 5]

with open('save.txt', 'w') as f:
    for item in mylist:
        f.write(str(item) + '\n')