import time
import os

def setup():
    print("\n")
    token = input("Please enter your Bot token\n")
    prefix = input("Please enter your Bot prefix\n")
    member = input("Please enter your Member ID\n")
    mod = input("Please enter your Moderator ID\n")
    admin = input("Please enter your Admin ID\n")
    guild = input("Please enter your Guild ID\n")
    log_channel = input("Please enter the channel ID for logs. (If you do not want to enable logs please press ENTER)\n")
    print("\n\n")
    print("Confirm with these values.")
    time.sleep(2)
    print(f"Token: {token}")
    print(f"Prefix: {prefix}")
    print(f"Member Role ID: {member}")
    print(f"Moderator Role ID: {mod}")
    print(f"Admin Role ID: {admin}")
    print(f"Guild ID: {guild}")
    print(f"Log Channel ID: {log_channel}")
    info_recheck = input("Is that information correct? [Y/N]\n")
    if info_recheck == "Y" or info_recheck == "y":
        print("Please wait while the bot is being setup.")
        with open(".env", "w") as env:
            env.write(f"TOKEN={token}" + "\n")
            env.write(f"PREFIX={prefix}" + "\n")
            env.write(f"MEMBER_ROLE={member}" + "\n")
            env.write(f"MODERATOR_ROLE={mod}" + "\n")
            env.write(f"ADMIN_ROLE={admin}" + "\n")
            env.write(f"GUILD_ID={guild}" + "\n")
            env.write(f"LOG_CHANNEL={log_channel}")
        if log_channel == "":
            os.chdir("cogs")
            os.remove("logs.py")
            os.chdir("..")
            print("File logs.py removed.")
            time.sleep(5)
            exit()
        else:
            print("Setup complete.")
            time.sleep(5)
            exit()
    if info_recheck == "N" or info_recheck == "n":
        print("Please restart the setup.")
        exit()

def tutorial():
    print("Welcome to the BeepBoopBot Tutorial! We will explain how to get every information needed for the setup here.")
    print("Token: Go to https://discord.com/developers/applications and click on your Application\n then click on the 'Bot' in left sidebar, click on 'Copy' under your Bot's name\n")
    print("Prefix: Enter the prefix you want for your bot\n")
    print("Member Role: Go to the Discord App, Right click on your Member role and click 'Copy ID'.\n")
    print("Moderator Role: Go to the Discord App, Right click on your Moderator role and click 'Copy ID'.\n")
    print("Admin Role: Go to the Discord App, Right click on your Admin role and click 'Copy ID'.\n")
    print("Guild ID: Go to the Discord App, Right click on your Guild and click 'Copy ID'.\n")
    print("Log Channel ID: Go to the Discord App, Right click on your Log Channel and click 'Copy ID'.\n")
    setup_after_tutorial = input("Do you want to go back to the setup? [Y/N]\n")
    if setup_after_tutorial == "Y" or setup_after_tutorial == "y":
        main()
    else:
        exit()

def setup_and_tutorial():
    print("Soon")

def main():
    print("Welcome to the BeepBoopBot setup.")
    main = input("Please chose from the following options:\n[1] Tutorial\n[2] Setup\n[3] Both\n[4] Exit\n")
    if main == "1":
        tutorial()
    if main == "2":
        setup()
    if main == "3":
        setup_and_tutorial()
    if main == "4":
        exit()
    else:
        print("Please enter a valid option.")
        main()


if __name__ == "__main__":
    main()