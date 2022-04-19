#average each two columns of array `data`


data = [[1,2,3], [4,5,6], [7,8,9]]

def average_columns(data):
    num_columns = len(data[0])
    for i in range(0, num_columns, 2):
        column1 = data[i]
        column2 = data[i+1]
        average = (column1 + column2) / 2
        print(average)