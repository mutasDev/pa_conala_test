#Remove all strings from a list a strings `sents` where the values starts with `@$\t` or `#`


sents = ['@$\tstring1', '#string2', 'string3']

for sent in sents:
    if sent.startswith('@$\t') or sent.startswith('#'):
        sents.remove(sent)

print(sents)