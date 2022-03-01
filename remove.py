# This file will remove all the dependencies
import os
import asyncio
import sys
import subprocess

print("Trying to remove dependencies using pip.")
print("This may take a while.")
os.system("pip uninstall python-dotenv -y")
os.system("pip uninstall datetime -y")
os.system("pip uninstall asyncio -y")
os.system("pip uninstall py-cord -y")

reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
if 'py-cord' in installed_packages:
    print("py-cord did not uninstall, trying to uninstall using pip3.")
    os.system("pip3 uninstall py-cord")
    if 'pycord' in installed_packages:
        print("Pycord still did not uninstall, trying to uninstall using common names.")
        os.system("pip3 uninstall pycord")
        os.system("pip3 uninstall pycord-discord")

if 'python-dotenv' in installed_packages:
    os.system("pip3 uninstall python-dotenv -y")

if 'datetime' in installed_packages:
    os.system("pip3 uninstall datetime -y")
if 'asyncio' in installed_packages:
    os.system("pip3 uninstall asyncio -y")

print("All dependencies have been removed.")
exit