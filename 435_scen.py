#Convert list of lists `data` into a flat list


data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat_list = [item for sublist in data for item in sublist]