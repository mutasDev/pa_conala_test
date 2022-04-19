#Sum integers contained in strings in list `['', '3.4', '', '', '1.0']`


result = 0
for i in ['', '3.4', '', '', '1.0']:
    if i.isdigit():
        result += int(i)
print(result)