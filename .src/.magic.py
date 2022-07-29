import os,sys

print("")
url = input("[?] Enter Full URL Address: ")
print("[!] Your Link is Ready: ")
os.system("curl https://tinyurl.com/api-create.php?url={0}\n\n".format(url))
