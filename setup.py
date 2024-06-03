import json
import requests

version = "0"
username = ""
reponame = ""
release_file = ""
requirements_file = False
requirements_file_name = ""
files = []

while True:
    username = input("Github Username: ")
    confirm = input(f"Is {username} correct? (y/n) ")
    if confirm[0].lower() == "y":
        break

while True:
    reponame = input("Repository name: ")
    confirm = input(f"Is {reponame} correct? (y/n) ")
    if confirm[0].lower() == "y":
        break

while True:
    release_file = input("What is your release file structure? If your file contains a version string, then use {version} in your answer, e.g. Release_{version}.zip, and the updater will substitute it in: ")
    confirm = input(f"Is {release_file} correct? (y/n) ")
    if confirm[0].lower() == "y":
        break

while True:
    _rf = input("Does your program use a requirements.txt file (y/n)? ")
    if _rf[0].lower() == "y":
        requirements_file = True
    else:
        requirements_file = False
    confirm = input(f"Is requirements={requirements_file} correct? (y/n) ")
    if confirm[0].lower() != "y":
        continue
    while True:
        _rfn = input("Is your requirements file called requirements.txt, or something else (press enter if it is called requirements.txt): ")
        if _rfn == "":
            requirements_file_name = "requirements.txt"
        else:
            requirements_file_name = _rfn
        confirm = input(f"Is {requirements_file_name} the correct name of your requirements file? (y/n) ")
        if confirm[0].lower() == "y":
            _break = True
            files.append(requirements_file_name)
            break
    if _break:
        break

while True:
    file_in_zip = input("Type the name of a file in your zip (if it is in a subfolder, use .\\folder\\filename.example, and do not include your requirements file).\nPress enter if you are done: ")
    if file_in_zip == "":
        break
    confirm = input(f"Is {file_in_zip} correct? (y/n) ")
    if confirm[0].lower() == "y":
        files.append(file_in_zip)
    for file in files:
        print(file)

with open("updater.json", "w") as u:
    upd = {}
    upd["version"] = version
    upd["uname"] = username
    upd["repo"] = reponame
    upd["rel_file"] = release_file
    upd["req_f"] = requirements_file
    upd["req_f_n"] = requirements_file_name
    upd["files"] = files
    json.dump(upd, u, indent=4)

updaterdl = requests.get("https://raw.githubusercontent.com/bazthedev/GithubUpdater/main/updater.py")
with open(".\\updater.py", "wb") as f:
    f.write(updaterdl.content)
    f.close()