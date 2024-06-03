# GithubUpdater
## A simple Python script that allows you to update your own programs via github releases.

## How to setup:
1. Download [setup.py](https://raw.githubusercontent.com/bazthedev/GithubUpdater/main/setup.py)
2. Run setup.py and follow the prompts
3. A file called `updater.json` will be generated, make sure you bundle this config with your program in the root, alongside `updater.py`, which is automatically downloaded after running setup.py
4. Simply run `updater.py` and it will check for new updates. If it is run for the first time, it will download the latest version of your program.

If you want your main program to contain update checking functionality, then simply add `from updater import check_update` to your code (if in python), and then run the `check_update()` function somewhere in your code.
