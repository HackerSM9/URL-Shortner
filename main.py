import os,sys

g = '\033[1;32m'
r = '\033[1;31m'
e = '\033[0m'

os.system("clear")
print('''
\033[0;34m██╗░░░██╗██████╗░██╗░░░░░              | Author : \033[1;33mHackerSM9\033[0m
\033[0;34m██║░░░██║██╔══██╗██║░░░░░              | Origin : \033[1;33mMade in India\033[0m
\033[0;34m██║░░░██║██████╔╝██║░░░░░              | Version : \033[1;33m1.0.0\033[0m
\033[0;34m██║░░░██║██╔══██╗██║░░░░░              | G-DEV : \033[1;33mHackerSM9\033[0m
\033[0;34m╚██████╔╝██║░░██║███████╗              | Twitter : \033[1;33mHackerSM9_\033[0m
\033[0;34m░╚═════╝░╚═╝░░╚═╝╚══════╝\033[0m
\033[0;31m╭━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━╮
╰━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━╯\033[0m
\033[1;34m╭━━━┳╮╱╱╱╱╱╱╭╮
┃╭━╮┃┃╱╱╱╱╱╭╯╰╮
┃╰━━┫╰━┳━━┳┻╮╭╋━╮╭━━┳━╮
╰━━╮┃╭╮┃╭╮┃╭┫┃┃╭╮┫┃━┫╭╯
┃╰━╯┃┃┃┃╰╯┃┃┃╰┫┃┃┃┃━┫┃
╰━━━┻╯╰┻━━┻╯╰━┻╯╰┻━━┻╯\033[0m
''')
print(g+"1) Short-URL/LINK\n2) More Tools\n3) About\n4) Upgrade\n"+e+r+"0) EXIT\n\n"+e)
url = int(input("\033[1;36m\n >> Enter your Choice: \033[0m"))
if (url == 1):
    os.system("cd .src && python3 .magic.py")
if (url == 2):
    os.system("xdg-open https://GitHub.com/HackerSM9")
if (url == 3):
    os.system("cd .src && python3 .about.py")
if (url == 4):
    os.system("bash update")
if (url == 0):
    print("Exited Successfully :)")
elif (url >= 5):
    print(r+"Invalid Option Ó╭╮Ò"+e)
else:
    print("\033[1;46mDone !\033[0m")
