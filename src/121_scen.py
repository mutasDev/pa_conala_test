#Get the characters count in a file `filepath`


def count_characters(filepath):
    with open(filepath) as f:
        return len(f.read())