#write multiple strings `line1`, `line2` and `line3` in one line in a file `target`


with open('target', 'w') as f:
    f.write('\n'.join(['line1', 'line2', 'line3']))