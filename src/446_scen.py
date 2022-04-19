#count number of times string 'brown' occurred in string 'The big brown fox is brown'


count = 0
for i in range(len('The big brown fox is brown')):
    if 'The big brown fox is brown'.startswith('brown', i):
        count += 1
print(count)