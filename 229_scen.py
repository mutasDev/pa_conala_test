#parse tab-delimited CSV file 'text.txt' into a list
 of lists.

import csv

with open('text.txt', 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    data = list(reader)