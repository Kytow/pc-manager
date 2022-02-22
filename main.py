# This project is old, the code is bad.
from os import listdir, system, mkdir, chdir, rename
from os.path import isdir
from colorama import Fore
from pycenter import center


def clear(): return system("cls")


print(center(f"""{Fore.LIGHTGREEN_EX}
██████   ██████     ███    ███  █████  ███    ██  █████   ██████  ███████ ██████
██   ██ ██          ████  ████ ██   ██ ████   ██ ██   ██ ██       ██      ██   ██
██████  ██          ██ ████ ██ ███████ ██ ██  ██ ███████ ██   ███ █████   ██████
██      ██          ██  ██  ██ ██   ██ ██  ██ ██ ██   ██ ██    ██ ██      ██   ██
██       ██████     ██      ██ ██   ██ ██   ████ ██   ██  ██████  ███████ ██   ██
\n
"""))

print(center(
    f"{Fore.RESET}[1] PC SORTER             [2] PC OPTIMIZER             [3] VIRUS SCANNER"))

while True:
    try:
        choice = int(input())
        break
    except:
        print(
            f"{Fore.RED}[!]{Fore.RESET} The choice isn't a number")


def sortFiles():
    files = listdir()
    filenumber = 0
    while True:
        try:
            uniquefile = files[filenumber]
        except:
            break
        filenumber = filenumber + 1
        splituniquefile = uniquefile.split(".")
        uniquefilebackslash = uniquefile.replace(" ", "_")
        try:
            rename(uniquefile, uniquefilebackslash)
        except:
            pass
        try:
            if splituniquefile[1] == "png" or splituniquefile[1] == "jpg" or splituniquefile[1] == "jpeg" or splituniquefile[1] == "gif" or splituniquefile[1] == "tiff":
                if not isdir("Picures"):
                    mkdir("Pictures")
                system(f"move {uniquefilebackslash} Pictures")
            elif splituniquefile[1] == "docx" or splituniquefile[1] == "doc" or splituniquefile[1] == "pdf" or splituniquefile[1] == "odt":
                if not isdir("Documents"):
                    mkdir("Documents")
                system(f"move {uniquefilebackslash} Documents")
            elif splituniquefile[1] == "zip" or splituniquefile[1] == "7z" or splituniquefile[1] == "rar":
                if not isdir("Compressed"):
                    mkdir("Compressed")
                system(f"move {uniquefilebackslash} Compressed")
            elif splituniquefile[1] == "mp4" or splituniquefile[1] == "flv" or splituniquefile[1] == "avi":
                if not isdir("Videos"):
                    mkdir("Videos")
                system(f"move {uniquefilebackslash} Videos")
            elif splituniquefile[1] == "mp3" or splituniquefile[1] == "wav":
                if not isdir("Music"):
                    mkdir("Music")
                system(f"move {uniquefilebackslash} Music")
            elif splituniquefile[1] == "exe":
                if not isdir("Executables"):
                    mkdir("Executables")
                system(f"move {uniquefilebackslash} Executables")
            else:
                pass
        except:
            pass


if choice == 1:
    # Asks the user for the directory to be stored
    while True:
        print("Which directory do you want to sort?")
        directoryclean = str(input())
        try:
            chdir(directoryclean)
            break
        except:
            print(
                f"{Fore.RED}[!]{Fore.RESET} The directory {directoryclean} isn't valid, exemple of directory : C:\\Users\\Kytow\\Downloads\\")

    sortFiles()


elif choice == 2:
    system("cleanmgr")
    clear()
elif choice == 3:
    system("mrt")
    clear()
else:
    quit()
