import os,sys

r = '\033[0m'
g = '\033[0m'
y = '\033[0m'
b = '\033[0m'
e = '\033[0m'

print("")
url = input("[?] Enter Full URL Address: ")
print("[✓] Your Link is Ready: ", end = "", flush = True)
os.system("curl https://tinyurl.com/api-create.php?url={0}".format(url))
print("\n")
