#python regex - check for a capital letter with a following lowercase in string `string`


if re.search(r'[A-Z][a-z]', string):
    print("There is a capital letter followed by a lowercase letter in the string.")
else:
    print("There is no capital letter followed by a lowercase letter in the string.")