#flatten list `list_of_menuitems`


list_of_menuitems = [["Coffee", "$2.50"], ["Tea", "$2.00"], ["Water", "$1.75"]]

for menuitem in list_of_menuitems:
    print(menuitem[0] + ": " + menuitem[1])