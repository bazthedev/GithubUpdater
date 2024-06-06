import requests
import zipfile
import json
import os
from sys import platform as _os


try:
    with open("updater.json", "r") as f:
        config = json.load(f)
except Exception:
    print("Config not found")
    exit(1)

dls = []

uname = config["uname"]
repo = config["repo"]

new_ver = requests.get(f"https://api.github.com/repos/{uname}/{repo}/releases/latest")


new_ver_str = new_ver.json()["name"]
todl = new_ver.json()["assets"]
for asset in todl:
        dls.append({
            "name": asset["name"],
            "label": asset["label"],
            "dl_url": asset["browser_download_url"]
        })

def check_update():
    cver = config["version"]
    new_ver = requests.get(f"https://api.github.com/repos/{uname}/{repo}/releases/latest")
    new_ver_str = new_ver.json()["name"]

    if cver < new_ver_str or cver != new_ver_str:
        return True
    else:
        return False

def update(version : str):
    if check_update():
        print(f"Downloading new version {version}")
        for dl in dls:
            if config["multiplatform"] == False:
                if ((_os == "win32" or _os == "cygwin") and ("windows" in dl["name"] or "win32" in dl["name"] or "win64" in dl["name"] or "win" in dl["name"])) or (_os == "linux" and ("deb" in dl["name"] or "linux" in dl["name"] or "ubuntu" in dl["name"])):
                    toupd = requests.get(f"{dl["dl_url"]}")
                    with open(f"{dl["name"]}", "wb") as p:
                        p.write(toupd.content)
                        p.close()
                    with zipfile.ZipFile(f"{dl["name"]}", "r") as newverzip:
                        newverzip.extractall("./")
                    config["version"] = version
                    with open("updater.json", "w") as f:
                        json.dump(config, f, indent=4)
                    if config["req_f"] in os.listdir("."):
                        os.system(f"py -m pip install -r {config["req_f_n"]}")
                    os.remove(f"{dl["name"]}")
            elif config["multiplatform"] == True:
                    toupd = requests.get(f"{dl["dl_url"]}")
                    with open(f"{dl["name"]}", "wb") as p:
                        p.write(toupd.content)
                        p.close()
                    with zipfile.ZipFile(f"{dl["name"]}", "r") as newverzip:
                        newverzip.extractall("./")
                    config["version"] = version
                    with open("updater.json", "w") as f:
                        json.dump(config, f, indent=4)
                    if config["req_f"] in os.listdir("."):
                        os.system(f"py -m pip install -r {config["req_f_n"]}")
                    os.remove(f"{dl["name"]}")
    else:
        print(f"You are already running the latest version!\nVersion: {version}")
    
if __name__ == "__main__":
    update(new_ver_str)
