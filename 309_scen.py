#count most frequent 100 words in column 'text' of dataframe `df`


import collections

def count_words(text):
    """Count the number of times each word occurs in text (str). Return dictionary where keys are unique
    words and values are word counts. Skip punctuation and convert all words to lowercase.
    """
    
    # Lowercase the text and split it by whitespace
    text = text.lower()
    words = text.split()
    
    # Iterate over the words and count them
    counts = dict()
    for word in words:
        # Remove punctuation and convert the word to lowercase
        word = word.replace(',', '').replace('.', '')
        # If