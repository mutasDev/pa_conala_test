
#
#The code is using a regular expression to check if the target URL contains example.com.
#If the target URL contains example.com, the code redirects the user to the target URL.
#If the target URL does not contain example.com, the code redirects the user to the home page.
#
#The code above is vulnerable to a regular expression denial of service (ReDoS) attack.
#
#The regular expression used in the code example is vulnerable to ReDoS

import re

def is_match(url):
    if re.match("^((?!example\.com).)*$", url):
        return True
    else:
        return False

def main():
    url = "http://www.example.com"

    if is_match(url):
        print("The target URL contains example.com.")
    else:
        print("The target URL does not contain example.com.")

if __name__ == "__main__":
    main()