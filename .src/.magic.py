import os,sys

r = '\033[0;31m'         
g = '\033[0;32m'        
y = '\033[0;33m'      
b = '\033[0;34m'      
v = '\033[0;35m'
e = '\033[0m'

print("")
url = input("y+[+e+r+?+e+y+]+y Enter Full URL Address: ")
print("+y+[+e+g✓+e+y]+e Your Link is Ready: ", end = "", flush = True)
os.system("curl https://tinyurl.com/api-create.php?url={0}".format(url))
print("\n")
