import os,sys

print("\n")
url = input(" [?] Enter Full URL Address: ")
print(" [!] Your Link is Ready: ")
os.system("curl https://tinyurl.com/api-create.php?url={0}".format(url))
