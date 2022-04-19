#replace dot characters  '.' associated with ascii letters in list `s` with space ' '


s = ['a.b', 'c.d', 'e.f']

for i in range(len(s)):
    s[i] = s[i].replace('.', ' ')

print(s)