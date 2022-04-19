#Reverse the order of words, delimited by `.`, in string `s`


s = "The quick brown fox jumps over the lazy dog."

words = s.split(" ")

reversed_words = words[::-1]

reversed_sentence = " ".join(reversed_words)

print(reversed_sentence)