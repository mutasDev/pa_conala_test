#convert list of string numbers into list of integers


numbers = ['1', '2', '3', '4', '5'] 

# function to convert string to integer 
def convert(s): 
	
	# checking if string is a number 
	if s.isdigit() == True: 
		
		# typecasting string to int 
		return int(s) 
	
	# if string is not a number 
	else: 
		
		# initializing empty list 
		new = [] 
		
		# traverse in the string 
		for i in range(len(s)): 
		