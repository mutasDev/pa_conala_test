#split a string `s` with into all strings of repeated characters


def split_string(s):
    return [''.join(c) for c in zip(*[s[i::i+1] for i in range(1, len(s))])]