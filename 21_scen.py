#convert a string `my_string` with dot and comma into a float number `my_float`


my_string = "1.234,5"

my_float = float(my_string.replace(",", "."))