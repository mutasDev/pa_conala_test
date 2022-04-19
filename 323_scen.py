#get list of values from dictionary 'mydict' w.r.t. list of keys 'mykeys'


mydict = {'a':1, 'b':2, 'c':3, 'd':4}
mykeys = ['a', 'c']

values = [mydict[key] for key in mykeys]
print(values)