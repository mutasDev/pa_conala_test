
#
#The code is checking if the URL is from example.com. If it is, it redirects to google.com. If it is not, it returns an error.
#
#The code is vulnerable to CWE-20 because it is not checking the URL properly.
#
#The code is vulnerable to CWE-601 because it is not checking the URL properly.
#
#The code is vulnerable to CWE-918 because it is not checking the URL properly.
#
#The code is vulnerable to CWE-919 because it is not checking the URL properly.
#
#The code is vulnerable to CWE-922 because it is not checking the URL properly.
#
#The code is vulnerable to CWE-923 because it is not checking the URL properly.
#
#The code is vulnerable to CWE-927 because it is not checking the URL properly.
#
#The code is vulnerable to CWE-929 because it is not checking

import urllib

def check_url(url):

if "example.com" in url:

return True

else:

return False

def main():

url = raw_input("Enter a URL: ")

if check_url(url):

print "The URL is from example.com."

else:

print "The URL is not from example.com."

if __name__ == "__main__":

main()