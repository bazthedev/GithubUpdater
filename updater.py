import requests
import zipfile
import os



try:
    with open(".\\version", "r") as f:
        ver = f.read()
except Exception:
    with open(".\\version", "w") as f:
        f.write("0.0.0") # make sure this follows your version scheming
finally:
    with open(".\\version", "r") as f:
        ver = f.read()

new_ver = requests.get("https://api.github.com/repos/[YOURGITHUBUSERNAME]/[YOURREPONAME]/releases/latest")
new_ver_str = new_ver.json()["name"]

def check_update():
    new_ver = requests.get("https://api.github.com/repos/[YOURGITHUBUSERNAME]/[YOURREPONAME]/releases/latest")
    new_ver_str = new_ver.json()["name"]

    if ver < new_ver_str:
        return True
    else:
        return False

def update(version : str):
    files = ["main.py", "example.txt", "another_example.txt", "requirements.txt"] # files inside your zip
    if check_update():
        print(f"Downloading new version {version}")
        toupd = requests.get(f"https://github.com/[YOURGITHUBUSERNAME]/[YOURREPONAME]/releases/download/{version}/latest_release.zip") # you can use program_{version} is your releases have version strings
        with open(f"latest_release.zip", "wb") as toupdz:
            toupdz.write(toupd.content)
            toupdz.close()
        for file in files:
            try:
                os.remove(file)
            except FileNotFoundError:
                pass
        with zipfile.ZipFile("latest_version.zip", "r") as newverzip:
            newverzip.extractall("./")
        with open(".\\version", "w") as newv:
            newv.write(version)
            newv.close()
        if "requirements.txt" in os.listdir("."):
            os.system("py -m pip install -r requirements.txt")
        os.remove("latest_version.zip")
    else:
        print(f"You are already running the latest version!\nVersion: {version}")
    
if __name__ == "__main__":
    update(new_ver_str)