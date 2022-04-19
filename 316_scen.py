#get all text that is not enclosed within square brackets in string `example_str`


example_str = "[this] is [an] example [string]"

result = re.findall(r'\[(.*?)\]', example_str)
print(result)