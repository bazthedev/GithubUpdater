import requests
import zipfile
import json
import os

def reset_config():
    with open("config.json", "w") as f:
        conf = {}
        conf["version"] = "0.0.0"
        conf["other_key"] = "example"
        json.dump(conf, f, indent=4)

try:
    with open("./config.json", "r") as f:
        config = json.load(f)
except Exception:
    reset_config()
finally:
    with open("./config.json", "r") as f:
        config = json.load(f)

cver = config["version"]

new_ver = requests.get("https://api.github.com/repos/[YOURGITHUBUSERNAME]/[YOURREPONAME]/releases/latest")
new_ver_str = new_ver.json()["name"]

def check_update():
    cver = config["version"]
    new_ver = requests.get("https://api.github.com/repos/[YOURGITHUBUSERNAME]/[YOURREPONAME]/releases/latest")
    new_ver_str = new_ver.json()["name"]

    if cver < new_ver_str:
        return True
    else:
        return False

def update(version : str):
    files = ["main.py", "example.txt", "another_example.txt", "requirements.txt"] # files inside your zip, if folder, do .\\foldername\\file
    if check_update():
        print(f"Downloading new version {version}")
        toupd = requests.get(f"https://github.com/[YOURGITHUBUSERNAME]/[YOURREPONAME]/releases/download/{version}/latest_release.zip") # you can use program_{version} is your releases have version strings
        with open("latest_version.zip", "wb") as p:
            p.write(toupd.content)
            p.close()
        for file in files:
            try:
                os.remove(file)
            except FileNotFoundError:
                pass
        with zipfile.ZipFile("latest_version.zip", "r") as newverzip:
            newverzip.extractall("./")
        config["version"] = version
        with open("./config.json", "w") as f:
            json.dump(config, f, indent=4)
        if "requirements.txt" in os.listdir("."):
            os.system("py -m pip install -r requirements.txt")
        os.remove("latest_version.zip")
    else:
        print(f"You are already running the latest version!\nVersion: {version}")
    
if __name__ == "__main__":
    update(new_ver_str)
