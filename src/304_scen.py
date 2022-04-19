#extract ip address from an html string


import re

def extract_ip(string):
  ip_address = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', string)
  return ip_address