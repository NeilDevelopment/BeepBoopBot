# This program will check your dependencies, if it dosen't find one it will install them. Only runs once.
import sys
import subprocess
import os

reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
if 'py-cord' not in installed_packages:
    print("py-cord is missing, installing...")
    os.system("pip3 install -U git+https://github.com/Pycord-Development/pycord > logs.txt")
    os.remove("logs.txt")
    print("Installed py-cord")
else:
    print("py-cord is already installed")
if "python-dotenv" not in installed_packages:
    print("python-dotenv is missing, installing...")
    os.system("pip3 install python-dotenv > logs.txt")
    os.remove("logs.txt")
    print("Installed python-dotenv")
else:
    print("python-dotenv is already installed")
if "asyncio" not in installed_packages:
    print("asyncio is missing, installing...")
    os.system("pip3 install asyncio > logs.txt")
    os.remove("logs.txt")
    print("Installed asyncio")
else:
    print("asyncio is already installed")
if "datetime" not in installed_packages:
    print("datetime is missing, installing...")
    os.system("pip3 install datetime > logs.txt")
    os.remove("logs.txt")
    print("Installed datetime")
else:
    print("datetime is already installed")
print("Installed all dependencies, now starting up the bot.")
os.remove("dependencie_checker.py")