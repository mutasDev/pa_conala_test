#capture final output of a chain of system commands `ps -ef | grep something | wc -l`


import subprocess

ps = subprocess.Popen(['ps', '-ef'], stdout=subprocess.PIPE)
grep = subprocess.Popen(['grep', 'something'], stdin=ps.stdout, stdout=subprocess.PIPE)
wc = subprocess.Popen(['wc', '-l'], stdin=grep.stdout, stdout=subprocess.PIPE)

output = wc.communicate()[0]