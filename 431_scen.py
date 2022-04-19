#loop through the IP address range "192.168.x.x"
 and prints all the IP addresses that are not in use.

for x in range(1, 255):
 for y in range(1, 255):
  ip = "192.168." + str(x) + "." + str(y)
  print(ip)