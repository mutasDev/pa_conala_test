#add a header to a csv file


import csv

with open('input.csv', 'r') as in_file:
    with open('output.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        reader = csv.reader(in_file)

        next(reader, None)  # skip the headers

        for row in reader:
            writer.writerow(row)