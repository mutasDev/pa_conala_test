#Create `list2` to contain the lists from list `list1` excluding the empty lists from `list1`


list1 = [["a", "b", "c"], [], ["d", "e", "f"], [], ["g", "h", "i"]]

list2 = [list1[i] for i in range(len(list1)) if list1[i] != []]