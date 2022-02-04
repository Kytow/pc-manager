from time import sleep
from os import listdir, system, mkdir, chdir, rename
from os.path import isdir
from pystyle import *
from pycenter import center


def clear(): return system("cls")


print(Colorate.Vertical(Colors.green_to_yellow, center("""
██████   ██████     ███    ███  █████  ███    ██  █████   ██████  ███████ ██████
██   ██ ██          ████  ████ ██   ██ ████   ██ ██   ██ ██       ██      ██   ██
██████  ██          ██ ████ ██ ███████ ██ ██  ██ ███████ ██   ███ █████   ██████
██      ██          ██  ██  ██ ██   ██ ██  ██ ██ ██   ██ ██    ██ ██      ██   ██
██       ██████     ██      ██ ██   ██ ██   ████ ██   ██  ██████  ███████ ██   ██
\n
""")))

print(center("[1] PC SORTER             [2] PC OPTIMIZER"))


pcchoice = int(input())

if pcchoice == 1:
    print("Directory to clean ?")
    directoryclean = str(input())
    chdir(directoryclean)
    files = listdir()
    filenumber = 0
    while True:
        try:
            uniquefile = files[filenumber]
        except:
            clear()
            print("Terminated ! The program'll close in 5 seconds")
            sleep(5)
            quit()
        filenumber = filenumber + 1
        splituniquefile = uniquefile.split(".")
        uniquefilebackslash = uniquefile.replace(" ", "_")
        try:
            rename(uniquefile, uniquefilebackslash)
        except:
            pass
        try:
            if splituniquefile[1] == "png" or splituniquefile[1] == "jpg" or splituniquefile[1] == "jpeg":
                if not isdir("Images"):
                    mkdir("Images")
                system(f"move {uniquefilebackslash} Images")
            elif splituniquefile[1] == "docx" or splituniquefile[1] == "doc" or splituniquefile[1] == "pdf":
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
                if not isdir("Musique"):
                    mkdir("Musique")
                system(f"move {uniquefilebackslash} Musique")
            else:
                pass
        except:
            pass

elif pcchoice == 2:
    system("cleanmgr")
    clear()
