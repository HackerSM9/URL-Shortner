import os,sys

r = '\033[1;31m'
g = '\033[0;32m'
y = '\033[1;33m'
b = '\033[0;34m'
v = '\033[0;35m'
e = '\033[0m'

q = '\033[0;33m[\033[0;31m?\033[0;33m]\033[0m'
i = '\033[0;33m[\033[0;32m!\033[0;33m]\033[0m'

print("")
url = input(q+" Enter Full URL Address: ")
print(i+" Your Link is Ready: \033[1;34m ", end = "", flush = True)
os.system("curl https://tinyurl.com/api-create.php?url={0}".format(url))
print("\n")
