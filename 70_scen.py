#get the last part of a string before the character '-'


def get_last_part(string):
    return string.rsplit('-', 1)[-1]