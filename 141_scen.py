#send the output of pprint object `dataobject` to file `logFile`


import pprint

dataobject = {'key1': 'value1', 'key2': 'value2'}

logFile = open('logFile.txt', 'w')

pprint.pprint(dataobject, logFile)

logFile.close()