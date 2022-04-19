#convert string `user_input` into a list of integers `user_list`


user_input = input("Enter a list of numbers: ")
user_list = user_input.split()
user_list = [int(i) for i in user_list]