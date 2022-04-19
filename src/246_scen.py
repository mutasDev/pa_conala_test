#length of longest element in list `words`


words = ['one', 'two', 'three', 'four', 'five']

longest = 0
for word in words:
    if len(word) > longest:
        longest = len(word)
print(longest)