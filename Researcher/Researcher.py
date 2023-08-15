# -*- coding: utf-8 -*-
"""
Author: new92
Github: @new92
Leetcode: @new92

Python script for retrieving the (possible) location of the followers of an Instagram user !
"""
try:
    import sys
    from time import sleep
    if sys.version_info[0] < 3:
        print("[!] Error ! This script requires Python version 3.X ! ")
        sleep(2)
        print("""[+] Instructions to download Python 3.x : 
        Linux: apt install python3
        Windows: https://www.python.org/downloads/
        MacOS: https://docs.python-guide.org/starting/install3/osx/""")
        sleep(3)
        print("[*] Please install the Python 3 and then use this script ✅")
        sleep(2)
        print("[+] Exiting...")
        sleep(1)
        quit(0)
    from tqdm import tqdm
    total_mods = 8
    bar = tqdm(total=total_mods, desc='Loading modules', unit='module')
    for _ in range(total_mods):
        sleep(0.75)
        bar.update(1)
    bar.close()
    import platform
    from os import system
    import os
    import json
    import instaloader
    import requests
except ImportError or ModuleNotFoundError:
    print("[!] WARNING: Not all packages used in Researcher have been installed !")
    sleep(2)
    print("[+] Ignoring warning...")
    sleep(1)
    if sys.platform.startswith('linux'):
        if os.geteuid() != 0:
            print("[!] Root user not detected !")
            sleep(2)
            print("[+] Trying to enable root user...")
            sleep(1)
            system("sudo su")
            try:
                system("sudo pip install -r requirements.txt")
            except Exception as ex:
                print("[!] Error ! Cannot install the required modules !")
                sleep(1)
                print(f"[=] Error message ==> {ex}")
                sleep(2)
                print("[1] Uninstall script")
                print("[2] Exit")
                opt=int(input("[>] Please enter a number (from the above ones): "))
                while opt < 1 or opt > 2 or opt == None:
                    if opt == None:
                        print("[!] This field can't be blank !")
                    else:
                        print("[!] Invalid number !")
                        sleep(1)
                        print("[+] Acceptable numbers: [1,2]")
                    sleep(1)
                    print("[1] Uninstall script")
                    print("[2] Exit")
                    opt=int(input("[>] Please enter again a number (from the above ones): "))
                if opt == 1:
                    def fpath(fname: str):
                        for root, dirs, files in os.walk('/'):
                            if fname in files:
                                return os.path.abspath(os.path.join(root, fname))
                        return None
                    def rmdir(dire):
                        DIRS = []
                        for root, dirs, files in os.walk(dire):
                            for file in files:
                                os.remove(os.path.join(root,file))
                            for dir in dirs:
                                DIRS.append(os.path.join(root,dir))
                        for i in range(len(DIRS)):
                            os.rmdir(DIRS[i])
                        os.rmdir(dire)
                    rmdir(fpath('InstaTools'))
                    print("[✓] Files and dependencies uninstalled successfully !")
                else:
                    print("[+] Exiting...")
                    sleep(1)
                    print("[+] See you next time 👋")
                    quit(0)
        else:
            system("sudo pip install -r requirements.txt")
    elif sys.platform == 'darwin':
        system("python -m pip install requirements.txt")
    elif platform.system() == 'Windows':
        system("pip install -r requirements.txt")

print("[✓] Successfully loaded modules !")
sleep(1)

def fpath(fname: str):
    for root, dirs, files in os.walk('/'):
        if fname in files:
            return os.path.abspath(os.path.join(root, fname))
    return None

def ScriptInfo():
    with open('config.json') as config:
        conf = json.load(config)
    f = conf['name'] + '.py'
    if os.path.exists(fpath(f)):
        fsize = os.stat(fpath(f)).st_size
    else:
        fsize = 0
    print(f"[+] Author: {conf['author']}")
    print(f"[+] Github: @{conf['author']}")
    print(f"[+] License: {conf['lice']}")
    print(f"[+] Natural language: {conf['lang']}")
    print(f"[+] Programming language(s) used: {conf['language']}")
    print(f"[+] Number of lines: {conf['lines']}")
    print(f"[+] Script's name: {conf['name']}")
    print(f"[+] API(s) used: {conf['api']}")
    print(f"[+] File size: {fsize} bytes")
    print(f"[+] File path: {fpath(f)}")
    print(f"|======|GITHUB REPO INFO|======|")
    print(f"[+] Stars: {conf['stars']}")
    print(f"[+] Forks: {conf['forks']}")
    print(f"[+] Open issues: {conf['issues']}")
    print(f"[+] Closed issues: {conf['clissues']}")
    print(f"[+] Open pull requests: {conf['prs']}")
    print(f"[+] Closed pull requests: {conf['clprs']}")
    print(f"[+] Discussions: {conf['discs']}")

def checkUser(user: str) -> bool:
    return user == None or len(user) > 30 or user == '' or user == ' '

def valUser(username: str) -> bool:
    return requests.get(f'https://www.instagram.com/{username}/', allow_redirects=False).status_code != 200

def nums():
    print("[1] Find location")
    print("[2] Show Reseacher's info and exit")
    print("[3] Uninstall Reseacher")
    print("[4] Exit")

def clear():
    if platform.system() == 'Windows':
        system('cls')
    else:
        system('clear')

def Uninstall() -> str:
    def rmdir(dire):
        DIRS = []
        for root, dirs, files in os.walk(dire):
            for file in files:
                os.remove(os.path.join(root,file))
            for dir in dirs:
                DIRS.append(os.path.join(root,dir))
        for i in range(len(DIRS)):
            os.rmdir(DIRS[i])
        os.rmdir(dire)
    rmdir(fpath('InstaTools'))
    return "[✓] Files and dependencies uninstalled successfully !"

def banner():
    return """
██████╗░███████╗░██████╗███████╗░█████╗░██████╗░░█████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██║░░██║██╔════╝██╔══██╗
██████╔╝█████╗░░╚█████╗░█████╗░░███████║██████╔╝██║░░╚═╝███████║█████╗░░██████╔╝
██╔══██╗██╔══╝░░░╚═══██╗██╔══╝░░██╔══██║██╔══██╗██║░░██╗██╔══██║██╔══╝░░██╔══██╗
██║░░██║███████╗██████╔╝███████╗██║░░██║██║░░██║╚█████╔╝██║░░██║███████╗██║░░██║
╚═╝░░╚═╝╚══════╝╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
"""

def main():
    print(banner())
    print("\n")
    print("[+] Author: new92")
    print("[+] Github: @new92")
    print("\n")
    print("[+] Researcher: Python script for retrieving the possible location of the followers of a user.")
    print("\n")
    nums()
    op=int(input("[::] Please enter a number (from the above ones): "))
    while op < 1 or op > 4:
        print("[!] Invalid number !")
        sleep(1)
        nums()
        sleep(1)
        op=int(input("[::] Please enter again a number (from the above ones): "))
    if op == 1:
        clear()
        print("[+] NOTE: The following username will be used to get the possible location of their followers.")
        sleep(4)
        username=str(input("[::] Please enter the username: "))
        while checkUser(username):
            if username == None or username == '' or username == ' ':
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid length !")
                sleep(1)
                print("[+] Acceptable username length: 30 or less characters")
            sleep(1)
            username=str(input("[::] Please enter again the username: "))
        username = username.lower().strip()
        while valUser(username):
            print("[!] User not found !")
            sleep(1)
            print("[1] Try with another username")
            print("[2] Return to menu")
            print("[3] Uninstall and Exit")
            opt=int(input("[::] Please enter a number (from the above ones): "))
            while opt < 1 or opt > 3 or opt == None:
                print("[!] Invalid number !")
                sleep(1)
                print("[1] Try with another username")
                print("[2] Return to menu")
                print("[3] Uninstall and Exit")
                opt=int(input("[::] Please enter again a number (from the above ones): "))
            if opt == 1:
                username=str(input("[::] Please enter the username: "))
                while checkUser(username):
                    if username == '' or username == None or username == ' ':
                        print("[!] This field can't be blank !")
                    else:
                        print("[!] Invalid length !")
                        sleep(1)
                        print("[+] Acceptable username length: 30 or less characters")
                    sleep(1)
                    username=str(input("[::] Please enter again the username: "))
            elif opt == 2:
                clear()
                main()
            else:
                clear()
                print(Uninstall())
                sleep(2)
                print("[+] Thank you for using my script 😁")
                sleep(2)
                print("[+] Hope you enjoyed it ! 👍")
                sleep(2)
                print("[+] Until next time 👋")
                sleep(1)
                quit(0)
        loc=str(input("[::] Please enter the location: "))
        while loc == None or loc == '':
            print("[!] Invalid location !")
            sleep(1)
            loc=str(input("[::] Please enter again the location: "))
        loc = loc.capitalize().strip()
        loader = instaloader.Instaloader()
        print("|"+"-"*20+"login".upper()+"-"*20+"|")
        user=str(input("[::] Please enter your username: "))
        while checkUser(user):
            if user == None or user == '' or user == ' ':
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid length !")
                sleep(1)
                print("[+] Acceptable username length: 30 or less characters")
            sleep(1)
            user=str(input("[::] Please enter again your username: "))
        user = user.lower().strip()
        while valUser(user):
            print("[!] User not found !")
            sleep(1)
            print("[1] Try with another username")
            print("[2] Return to menu")
            print("[3] Uninstall and Exit")
            opt=int(input("[::] Please enter a number (from the above ones): "))
            while opt < 1 or opt > 3 or opt == None:
                print("[!] Invalid number !")
                sleep(1)
                print("[1] Try with another username")
                print("[2] Return to menu")
                print("[3] Uninstall and Exit")
                opt=int(input("[::] Please enter again a number (from the above ones): "))
            if opt == 1:
                username=str(input("[::] Please enter the username: "))
                while checkUser(username):
                    if username == None or username == '' or username == ' ':
                        print("[!] This field can't be blank !")
                    else:
                        print("[!] Invalid length !")
                        sleep(1)
                        print("[+] Acceptable username length: 30 or less characters")
                    sleep(1)
                    username=str(input("[::] Please enter again the username: "))
            elif opt == 2:
                clear()
                main()
            else:
                clear()
                print(Uninstall())
                sleep(2)
                print("[+] Thank you for using my script 😁")
                sleep(2)
                print("[+] Until we meet again 🫡")
                sleep(1)
                quit(0)
        passw=str(input("[::] Please enter your password: "))
        while passw == None or passw == '':
            print("[!] You must enter a password !")
            sleep(1)
            passw=str(input("[::] Please enter again your password: "))
        print("|"+"-"*45+"|")
        try:
            loader.login(user,passw)
        except Exception as ex:
            print("[!] Login Error !")
            sleep(1)
            print(f"[*] Error message ==> {ex}")
            sleep(2)
            print("[+] Exiting...")
            quit(0)
        profile = instaloader.Profile.from_username(loader.context, username)
        followers = [follower.username for follower in profile.get_followers()]
        LIST = []
        for i in range(len(followers)):
            profile = instaloader.Profile.from_username(loader.context, followers[i])
            if loc in profile.biography:
                LIST.append(followers[i])
        if len(LIST) == 0:
            print(f"[!] No users with such location found on the followers of {username}")
            sleep(3)
            print("[+] Exiting...")
            quit(0)
        else:
            per = (float(len(followers)) / len(LIST)) * 100
            name = f'users_in_{loc}.txt'
            f = open(name,"w")
            print(f"[+] Location: {loc}")
            print(f"[+] Searched in user's: {username} followers")
            print(f"[+] {len(LIST)} users in location: {loc}")
            print(f"[+] Percentage of users with this location: {per}%")
            print("|"+"-"*20+"users".upper()+"-"*20+"|")
            for i in range(len(LIST)):
                print(f"[=] Username: {LIST[i]}")
                f.write(f"[=] Username: {LIST[i]}")
                f.write("\n")
            f.close()
            print("[✓] Successfully saved usersnames !")
            sleep(1)
            print(f"[↪] File name: {name}")
            print(f"[↪] Path: {fpath(name)}")
            print(f"[↪] File size: {os.stat(fpath(name)).st_size} bytes")
            sleep(3)

    elif op == 2:
        clear()
        ScriptInfo()
        print("\n\n")

    elif op == 3:
        clear()
        print(Uninstall())
        sleep(2)
        print("[+] Thank you for using Researcher 😁")
        sleep(2)
        print("[+] Until we meet again 🫡")
        sleep(1)
        quit(0)

    else:
        clear()
        print("[+] Thank you for using Researcher 😁")
        sleep(2)
        print("[+] See you next time 👋")
        sleep(1)
        quit(0)
    print("[1] Return to menu")
    print("[2] Exit")
    number=int(input("[::] Please enter a number (from the above ones): "))
    while number < 1 or number > 2 or number == None:
        if number == None:
            print("[!] This field can't be blank !")
        else:
            print("[!] Invalid number !")
        number=int(input("[::] Please enter again a number (from the above ones): "))
    if number == 1:
        clear()
        main()
    else:
        print("[+] Exiting...")
        sleep(1)
        print("[+] See you next time 👋")
        sleep(2)
        quit(0)

if __name__ == '__main__':
    main()
