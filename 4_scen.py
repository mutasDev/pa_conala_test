#How to convert a string from CP-1251 to UTF-8?


# -*- coding: cp1251 -*-

s = 'Алексей'

u = s.decode('cp1251')

print(u.encode('utf8'))