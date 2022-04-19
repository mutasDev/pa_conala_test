#remove all special characters, punctuation and spaces from a string `mystring` using regex


re.sub('[^A-Za-z0-9]+', '', mystring)