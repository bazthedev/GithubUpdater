import json
import requests

version = "0"
username = ""
reponame = ""
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

print("Generating config...")

with open("updater.json", "w") as u:
    upd = {}
    upd["version"] = version
    upd["uname"] = username
    upd["repo"] = reponame
    upd["req_f"] = requirements_file
    upd["req_f_n"] = requirements_file_name
    json.dump(upd, u, indent=4)

updaterdl = requests.get("https://raw.githubusercontent.com/bazthedev/GithubUpdater/main/updater.py")
with open(".\\updater.py", "wb") as f:
    f.write(updaterdl.content)
    f.close()

print("Done")
