from colorama import Fore, Style
import os, platform, subprocess, sys

def variables():
    pass


""" If the install kwarg is set to "False" it will check for dependencies,
if it is set to "True" it will install dependencies.
"""
operatingsystem = platform.system()
def dependencies(*, install):
    if install == True:
        print(Fore.BLUE + "Installing dependencies!")
        try:
            if operatingsystem != "Windows":
                os.system("pip3 install DateTime")
            else:
                os.system("pip install DateTime")
        except:
            print("There was an error while installing \"DateTime\".")
        try:
            if operatingsystem != "Windows":
                os.system("pip3 install py-cord==2.0.0b1")
            else:
                os.system("pip install py-cord==2.0.0b1")
        except:
            print("There was an error while installing \"py-cord\".")
        try:
            if operatingsystem != "Windows":
                os.system("pip3 install asyncio")
            else:
                os.system("pip install asyncio")
        except:
            print("There was an error while installing \"asyncio\".")
        try:
            if operatingsystem != "Windows":
                os.system("pip3 install python-dotenv")
            else:
                os.system("pip install python-dotenv")
        except:
            print("There was an error while installing \"python-dotenv\".")
    else:
        reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
        installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
        if 'py-cord' not in installed_packages:
            if operatingsystem != "Windows:":
                print(Fore.RED + "Module \"py-cord\" is missing! Install it by doing pip install py-cord==2.0.0b1\n" + Fore.BLUE + "Please make sure to have the " + Fore.GREEN + "\"==2.0.0\"" + Fore.BLUE + " or it won't work!") 
            else:
                print(Fore.RED + "Module \"py-cord\" is missing! Install it by doing pip3 install py-cord==2.0.0b1") 
        else:
            pass
        if "python-dotenv" not in installed_packages:
            if operatingsystem != "Windows:":
                print(Fore.RED + "Module \"python-dotenv\" is missing! Install it by doing pip install python-dotenv") 
            else:
                print(Fore.RED + "Module \"python-dotenv\" is missing! Install it by doing pip3 install python-dotenv") 
        else:
            pass
        if "asyncio" not in installed_packages:
            if operatingsystem != "Windows:":
                print(Fore.RED + "Module \"asyncio\" is missing! Install it by doing pip install asyncio") 
            else:
                print(Fore.RED + "Module \"asyncio\" is missing! Install it by doing pip3 install asyncio") 
        else:
            pass
        if "DateTime" not in installed_packages:
            if operatingsystem != "Windows:":
                print(Fore.RED + "Module \"datetime\" is missing! Install it by doing pip install datetime") 
            else:
                print(Fore.RED + "Module \"datetime\" is missing! Install it by doing pip3 install datetime") 
        else:
            pass
def all():
    dependencies()
    variables()

if __name__ == "__main__":
    all()
