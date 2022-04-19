#Extract brackets from string `s`


s = "[this] [is] [a] [test]"

result = []

for i in range(len(s)):
    if s[i] == "[":
        result.append(i)
    elif s[i] == "]":
        result.append(i)

print(result)