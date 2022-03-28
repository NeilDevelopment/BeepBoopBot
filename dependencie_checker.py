# This program will check your dependencies, if it dosen't find one it will install them. Only runs once.
import sys
import subprocess
import os
import platform
from colorama import Fore, Back, Style

operatingsystem = platform.system()

reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
if 'py-cord' not in installed_packages:
    if operatingsystem != "Windows:":
        print(Fore.RED + "py-cord is missing, installing...")
        os.system("pip3 install py-cord==2.0.0b1 > logs.txt")
        os.remove("logs.txt")
        print(Fore.GREEN + "Installed py-cord")
    else:
        print(Fore.RED + "py-cord is missing, installing...")
        os.system("pip install py-cord==2.0.0b1 > logs.txt")
        os.remove("logs.txt")
        print(Fore.GREEN + "Installed py-cord")
else:
    print(Fore.GREEN + "py-cord is already installed")
if "python-dotenv" not in installed_packages:
    if operatingsystem != "Windows:":
        print(Fore.RED + "python-dotenv is missing, installing...")
        os.system("pip3 install python-dotenv > logs.txt")
        os.remove("logs.txt")
        print(Fore.GREEN + "Installed python-dotenv")
    else:
        print(Fore.RED + "python-dotenv is missing, installing...")
        os.system("pip install python-dotenv > logs.txt")
        os.remove("logs.txt")
        print(Fore.GREEN + "Installed python-dotenv")
else:
    print(Fore.GREEN + "python-dotenv is already installed")
if "asyncio" not in installed_packages:
    if operatingsystem != "Windows:":
        print(Fore.RED + "asyncio is missing, installing...")
        os.system("pip3 install asyncio > logs.txt")
        os.remove("logs.txt")
        print(Fore.GREEN + "Installed asyncio")
    else:
        print(Fore.RED + "asyncio is missing, installing...")
        os.system("pip install asyncio > logs.txt")
        os.remove("logs.txt")
        print(Fore.GREEN + "Installed asyncio")
else:
    print(Fore.GREEN + "asyncio is already installed")
if "datetime" not in installed_packages:
    if operatingsystem != "Windows:":
        print(Fore.RED + "datetime is missing, installing...")
        os.system("pip3 install datetime > logs.txt")
        os.remove("logs.txt")
        print(Fore.GREEN + "Installed datetime")
    else:
        print(Fore.RED + "datetime is missing, installing...")
        os.system("pip install datetime > logs.txt")
        os.remove("logs.txt")
        print(Fore.GREEN + "Installed datetime")
else:
    print(Fore.GREEN + "py-cord is already installed")
print("Installed all dependencies, now starting up the bot.")
exit()