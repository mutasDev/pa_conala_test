#check characters of string `string` are true predication of function `predicate`


def check_characters(string, predicate):
  for char in string:
    if not predicate(char):
      return False
  return True