
#
#The code is using a regular expression to check if the target URL contains example.com.
#If the target URL contains example.com, the code redirects the user to the target URL.
#If the target URL does not contain example.com, the code redirects the user to the home page.
#
#The code above is vulnerable to a regular expression denial of service (ReDoS) attack.
#
#The regular expression used in the code example is vulnerable to ReDoS because it contains nested quantifiers.
#
#The regular expression r'.*example\.com' is vulnerable to ReDoS because it contains nested quantifiers.
#
#The regular expression r'.*example\.com' is vulnerable to ReDoS because it contains nested quantifiers.
#
#The regular expression r'.*example\.com' is vulnerable to ReDoS because it contains nested quantifiers.
#
#The regular expression r'.*example\.com' is vulnerable to ReDoS because it contains nested

import re

def check_url(url):
    if re.match(r'.*example\.com', url):
        return True
    else:
        return False

def main():
    url = input('Enter a URL: ')
    if check_url(url):
        print('The URL is valid')
    else:
        print('The URL is invalid')

if __name__ == '__main__':
    main()