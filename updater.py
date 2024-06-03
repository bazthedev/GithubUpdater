import requests
import zipfile
import json
import os


try:
    with open(".\\updater.json", "r") as f:
        config = json.load(f)
except Exception:
    print("Config not found")
    exit(1)
finally:
    with open(".\\updater.json", "r") as f:
        config = json.load(f)

uname = config["uname"]
repo = config["repo"]

new_ver = requests.get(f"https://api.github.com/repos/{uname}/{repo}/releases/latest")
new_ver_str = new_ver.json()["name"]

def check_update():
    cver = config["version"]
    new_ver = requests.get(f"https://api.github.com/repos/{uname}/{repo}/releases/latest")
    new_ver_str = new_ver.json()["name"]

    if cver < new_ver_str:
        return True
    else:
        return False

def update(version : str):
    files = config["files"]
    if check_update():
        print(f"Downloading new version {version}")
        if "{version}" in config["rel_file"]:
            dlf = config["rel_file"].replace("{version}", f"{version}")
        else:
            dlf = config["rel_file"]
        toupd = requests.get(f"https://github.com/{uname}/{repo}/releases/download/{version}/{dlf}") # you can use program_{version} is your releases have version strings
        with open(f"{config["rel_file"]}", "wb") as p:
            p.write(toupd.content)
            p.close()
        for file in files:
            try:
                os.remove(file)
            except FileNotFoundError:
                pass
        with zipfile.ZipFile(f"{config["rel_file"]}", "r") as newverzip:
            newverzip.extractall("./")
        config["version"] = version
        with open(".\\updater.json", "w") as f:
            json.dump(config, f, indent=4)
        if config["req_f"] in os.listdir("."):
            os.system(f"py -m pip install -r {config["req_f_n"]}")
        os.remove(f".\\{config["rel_file"]}")
    else:
        print(f"You are already running the latest version!\nVersion: {version}")
    
if __name__ == "__main__":
    update(new_ver_str)
