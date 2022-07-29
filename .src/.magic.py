import os,sys

r = ''
g = ''
y = ''
b = ''

print("")
url = input("[?] Enter Full URL Address: ")
print("[✓] Your Link is Ready: ", end = "", flush = True)
os.system("curl https://tinyurl.com/api-create.php?url={0}".format(url))
print("\n")
