from colorama import Fore, Style
import os, platform, subprocess, sys, time

operatingsystem = platform.system()
def variables(*, copy=True):
    if copy == True:
        if operatingsystem != "Windows":
            os.system("cp example.env .env")
        else:
            os.system("copy example.env .env")
        token = input(Fore.GREEN + "Please enter your Bot token\nSteps: Go to https://discord.com/developers/applications and click on your Application\nthen click on the 'Bot' in left sidebar, click on 'Copy' under your Bot's name\n" + Fore.BLUE)
        mod = input(Fore.GREEN + "Please enter your Moderator Role ID\nSteps: Go to the Discord App, Right click on your Moderator role and click 'Copy ID'.\n" + Fore.BLUE)
        admin = input(Fore.GREEN + "Please enter your Admin Role ID\nSteps: Go to the Discord App, Right click on your Admin role and click 'Copy ID'.\n" + Fore.BLUE)
        guild = input(Fore.GREEN + "Please enter your Guild ID\nSteps: Go to the Discord App, Right click on your Guild and click 'Copy ID'.\n" + Fore.BLUE)
        log_channel = input(Fore.GREEN + "Please enter the channel ID for logs.\nSteps: Go to the Discord App, Right click on your Log Channel and click 'Copy ID'.\n" + Fore.BLUE)
        devmode = input(Fore.GREEN + "Do you want to enable developer mode? [Y/N]\n" + Fore.BLUE)
        if devmode.lower() == "y":
            print(Fore.GREEN + "Enabled developer mode!\n")
            pastebin_key = input(Fore.GREEN + "Please enter your Paste bin API Key.\nSteps: Go to https://pastebin.com/doc_api#1 and copy your API Key from there(You must have an account to see the API Key)\n"+ Fore.BLUE)
            print("\n\n")
            print("Confirm with these values.")
            time.sleep(2)
            print(f"{Fore.GREEN}Token: {Fore.BLUE}{token}")
            print(f"{Fore.GREEN}Moderator Role ID: {Fore.BLUE}{mod}")
            print(f"{Fore.GREEN}Admin Role ID: {Fore.BLUE}{admin}")
            print(f"{Fore.GREEN}Guild ID: {Fore.BLUE}{guild}")
            print(f"{Fore.GREEN}Log Channel ID: {Fore.BLUE}{log_channel}")
            print(f"{Fore.GREEN}Paste bin KEY: {Fore.BLUE}{pastebin_key}")
            info_recheck = input("Is that information correct? [Y/N]\n")
            if info_recheck == "Y" or info_recheck == "y":
                print("Please wait while the bot is being setup.")
                with open(".env", "w") as env:
                    env.write(f"TOKEN={token}" + "\n")
                    env.write(f"MODERATOR_ROLE={mod}" + "\n")
                    env.write(f"ADMIN_ROLE={admin}" + "\n")
                    env.write(f"GUILD_ID={guild}" + "\n")
                    env.write(f"LOG_CHANNEL={log_channel}\n")
                    env.write(f"PASTEBIN_API_KEY={pastebin_key}\n")
                    env.write("DEV_MODE=YES")
                    print("Setup complete.")
                    time.sleep(5)
                    exit()
            if info_recheck == "N" or info_recheck == "n":
                restart = input("Would you like to restart the setup? [Y/N] \n" + Fore.BLUE)
                if restart.lower() == "y":
                    variables(copy=False)
                else:
                    exit()
        else:
            os.chdir("developer")
            os.remove("run.py")
            os.chdir("..")
            print("\n\n")
            print("Confirm with these values.")
            time.sleep(2)
            print(f"{Fore.GREEN}Token: {Fore.BLUE}{token}")
            print(f"{Fore.GREEN}Moderator Role ID: {Fore.BLUE}{mod}")
            print(f"{Fore.GREEN}Admin Role ID: {Fore.BLUE}{admin}")
            print(f"{Fore.GREEN}Guild ID: {Fore.BLUE}{guild}")
            print(f"{Fore.GREEN}Log Channel ID: {Fore.BLUE}{log_channel}")
            info_recheck = input("Is that information correct? [Y/N]\n")
            if info_recheck == "Y" or info_recheck == "y":
                print("Please wait while the bot is being setup.")
                with open(".env", "w") as env:
                    env.write(f"TOKEN={token}" + "\n")
                    env.write(f"MODERATOR_ROLE={mod}" + "\n")
                    env.write(f"ADMIN_ROLE={admin}" + "\n")
                    env.write(f"GUILD_ID={guild}" + "\n")
                    env.write(f"LOG_CHANNEL={log_channel}\n")
                    env.write("DEV_MODE=NO")
                    print("Setup complete.")
                    time.sleep(5)
                    exit()
            if info_recheck == "N" or info_recheck == "n":
                restart = input("Would you like to restart the setup? [Y/N] \n" + Fore.BLUE)
                if restart.lower() == "y":
                    variables(copy=False)
                else:
                    exit()
    else:
        token = input(Fore.GREEN + "Please enter your Bot token\nSteps: Go to https://discord.com/developers/applications and click on your Application\nthen click on the 'Bot' in left sidebar, click on 'Copy' under your Bot's name\n" + Fore.BLUE)
        mod = input(Fore.GREEN + "Please enter your Moderator Role ID\nSteps: Go to the Discord App, Right click on your Moderator role and click 'Copy ID'.\n" + Fore.BLUE)
        admin = input(Fore.GREEN + "Please enter your Admin Role ID\nSteps: Go to the Discord App, Right click on your Admin role and click 'Copy ID'.\n" + Fore.BLUE)
        guild = input(Fore.GREEN + "Please enter your Guild ID\nSteps: Go to the Discord App, Right click on your Guild and click 'Copy ID'.\n" + Fore.BLUE)
        log_channel = input(Fore.GREEN + "Please enter the channel ID for logs.\nSteps: Go to the Discord App, Right click on your Log Channel and click 'Copy ID'.\n" + Fore.BLUE)
        devmode = input(Fore.GREEN + "Do you want to enable developer mode? [Y/N]\n" + Fore.BLUE)
        if devmode.lower() == "y":
            print(Fore.GREEN + "Enabled developer mode!\n")
            pastebin_key = input(Fore.GREEN + "Please enter your Paste bin API Key.\nSteps: Go to https://pastebin.com/doc_api#1 and copy your API Key from there(You must have an account to see the API Key)\n"+ Fore.BLUE)
            print("\n\n")
            print("Confirm with these values.")
            time.sleep(2)
            print(f"{Fore.GREEN}Token: {Fore.BLUE}{token}")
            print(f"{Fore.GREEN}Moderator Role ID: {Fore.BLUE}{mod}")
            print(f"{Fore.GREEN}Admin Role ID: {Fore.BLUE}{admin}")
            print(f"{Fore.GREEN}Guild ID: {Fore.BLUE}{guild}")
            print(f"{Fore.GREEN}Log Channel ID: {Fore.BLUE}{log_channel}")
            print(f"{Fore.GREEN}Paste bin KEY: {Fore.BLUE}{pastebin_key}")
            info_recheck = input("Is that information correct? [Y/N]\n")
            if info_recheck == "Y" or info_recheck == "y":
                print("Please wait while the bot is being setup.")
                with open(".env", "w") as env:
                    env.write(f"TOKEN={token}" + "\n")
                    env.write(f"MODERATOR_ROLE={mod}" + "\n")
                    env.write(f"ADMIN_ROLE={admin}" + "\n")
                    env.write(f"GUILD_ID={guild}" + "\n")
                    env.write(f"LOG_CHANNEL={log_channel}\n")
                    env.write(f"PASTEBIN_API_KEY={pastebin_key}\n")
                    env.write("DEV_MODE=YES")
                    print("Setup complete.")
                    time.sleep(5)
                    exit()
            if info_recheck == "N" or info_recheck == "n":
                restart = input("Would you like to restart the setup? [Y/N] \n" + Fore.BLUE)
                if restart.lower() == "y":
                    variables(copy=False)
                else:
                    exit()
        else:
            os.chdir("developer")
            os.remove("run.py")
            os.chdir("..")
            print("\n\n")
            print("Confirm with these values.")
            time.sleep(2)
            print(f"{Fore.GREEN}Token: {Fore.BLUE}{token}")
            print(f"{Fore.GREEN}Moderator Role ID: {Fore.BLUE}{mod}")
            print(f"{Fore.GREEN}Admin Role ID: {Fore.BLUE}{admin}")
            print(f"{Fore.GREEN}Guild ID: {Fore.BLUE}{guild}")
            print(f"{Fore.GREEN}Log Channel ID: {Fore.BLUE}{log_channel}")
            info_recheck = input("Is that information correct? [Y/N]\n")
            if info_recheck == "Y" or info_recheck == "y":
                print("Please wait while the bot is being setup.")
                with open(".env", "w") as env:
                    env.write(f"TOKEN={token}" + "\n")
                    env.write(f"MODERATOR_ROLE={mod}" + "\n")
                    env.write(f"ADMIN_ROLE={admin}" + "\n")
                    env.write(f"GUILD_ID={guild}" + "\n")
                    env.write(f"LOG_CHANNEL={log_channel}\n")
                    env.write("DEV_MODE=NO")
                    print("Setup complete.")
                    time.sleep(5)
                    exit()
            if info_recheck == "N" or info_recheck == "n":
                restart = input("Would you like to restart the setup? [Y/N] \n" + Fore.BLUE)
                if restart.lower() == "y":
                    variables(copy=False)
                else:
                    exit()

""" If the install kwarg is set to "False" it will check for dependencies,
if it is set to "True" it will install dependencies.
"""

def dependencies(*, install):
    if install == True:
        print(Fore.BLUE + "Installing dependencies!")
        try:
            if operatingsystem != "Windows":
                os.system("pip3 install DateTime > pip-logs.txt")
                os.remove("pip-logs.txt")
            else:
                os.system("pip install DateTime > pip-logs.txt")
                os.remove("pip-logs.txt")
        except:
            print("There was an error while installing \"DateTime\".")
        try:
            if operatingsystem != "Windows":
                os.system("pip3 install py-cord==2.0.0b1 > pip-logs.txt")
                os.remove("pip-logs.txt")
            else:
                os.system("pip install py-cord==2.0.0b1 > pip-logs.txt")
                os.remove("pip-logs.txt")
        except:
            print("There was an error while installing \"py-cord\".")
        try:
            if operatingsystem != "Windows":
                os.system("pip3 install asyncio > pip-logs.txt")
                os.remove("pip-logs.txt")
            else:
                os.system("pip install asyncio > pip-logs.txt")
                os.remove("pip-logs.txt")
        except:
            print("There was an error while installing \"asyncio\".")
        try:
            if operatingsystem != "Windows":
                os.system("pip3 install python-dotenv > pip-logs.txt")
                os.remove("pip-logs.txt")
            else:
                os.system("pip install python-dotenv > pip-logs.txt")
                os.remove("pip-logs.txt")
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
    variables()


if __name__ == "__main__":
    all()
