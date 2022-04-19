#create a list containing flattened list `[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]`


`list1 = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]`
`list2 = [i for l in list1 for i in l]`
`print(list2)`