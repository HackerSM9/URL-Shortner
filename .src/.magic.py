import os,sys

e = '\033[0m'
q = '\033[0;33m[\033[1;31m?\033[0;33m]\033[0m'
i = '\033[0;33m[\033[0;32m!\033[0;33m]\033[0m'

print("")
url = input(q+" Enter Full URL Address: ")
print("")
print(i+" Your Link is Ready: \033[1;34m ", end = "", flush = True)
os.system("curl https://tinyurl.com/api-create.php?url={0}".format(url))
print(e+"\n")
