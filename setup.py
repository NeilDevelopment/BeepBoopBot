import time
import os

def main():
    print("Welcome to the BeepBoopBot setup.")
    print("If you do not know how to get this information please go to \nhttps://u.neildevolopment.ml/beepboopbot/wiki/configuration")
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


if __name__ == "__main__":
    main()