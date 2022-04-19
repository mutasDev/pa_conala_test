#get digits only from a string `aas30dsa20` using lambda function


aas30dsa20 = ''.join(filter(lambda x: x.isdigit(), aas30dsa20))