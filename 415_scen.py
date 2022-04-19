#read a file 'C:/name/MyDocuments/numbers' into a list `data`


with open('C:/name/MyDocuments/numbers') as f:
    data = [int(x) for x in f]