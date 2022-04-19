#split string 'Words, words, words.' using a regex '(\\W+)'
 and prints the list of words in the order they appear in the string

words = 'Words, words, words.'

print(re.split('(\\W+)', words))