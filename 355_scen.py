#sort list `li` in descending order based on the date value in second element of each list in list `li`


li = [["John", "2018-01-02"], ["Adam", "2018-01-01"], ["Smith", "2018-01-03"]]

li.sort(key=lambda x: x[1], reverse=True)