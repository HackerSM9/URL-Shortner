import os,sys

g = '\033[32m'
r = '\033[1;31m'
e = '\033[0m'
os.system("clear")
print('''
██╗░░░██╗██████╗░██╗░░░░░░░░░░░░██████╗██╗░░██╗░█████╗░██████╗░████████╗███╗░░██╗███████╗██████╗░
██║░░░██║██╔══██╗██║░░░░░░░░░░░██╔════╝██║░░██║██╔══██╗██╔══██╗╚══██╔══╝████╗░██║██╔════╝██╔══██╗
██║░░░██║██████╔╝██║░░░░░█████╗╚█████╗░███████║██║░░██║██████╔╝░░░██║░░░██╔██╗██║█████╗░░██████╔╝
██║░░░██║██╔══██╗██║░░░░░╚════╝░╚═══██╗██╔══██║██║░░██║██╔══██╗░░░██║░░░██║╚████║██╔══╝░░██╔══██╗
╚██████╔╝██║░░██║███████╗░░░░░░██████╔╝██║░░██║╚█████╔╝██║░░██║░░░██║░░░██║░╚███║███████╗██║░░██║
░╚═════╝░╚═╝░░╚═╝╚══════╝░░░░░░╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝

                                             <---[ by HackerSM9 ]--->
''')
print(g+"1) Short-URL/LINK\n2) More Tools\n3) About\n"+e+r+"0) EXIT\n\n"+e)
url = int(input("\033[1;36m\n >> Enter your Choice: \033[0m"))
if (url == 1):
    os.system("cd .src && python3 .magic.py")
if (url == 2):
    os.system("xdg-open https://GitHub.com/HackerSM9")
if (url == 3):
    os.system("cd .src && python3 .about.py")
if (url == 0):
    os.system("logout || exit")
elif (url >= 4):
     print("Invalid Option Ó╭╮Ò")
else:
     print("\033[1;46mDone !\033[0m")
