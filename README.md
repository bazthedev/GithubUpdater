# GithubUpdater
## A simple Python script that allows you to update your own programs via github releases.

## How to use:
1. Choose if your program will use a config.json (updater_w_config) or a file which contains the version inside (updater)
2. Change `[YOURGITHUBUSERNAME]` and `[YOURREPONAME]` to your Github username and your Repository name
3. Edit the files in the `files` list to the files which will be inside your release zip
4. Change `latest_release.zip` to however your releases are structured, if your filename contains a version string, then add {version} to the name
5. Change `0.0.0` to a string before your first release, e.g. if it is 0.1, change it to 0.0
6. If you want your main program to contain update checking functionality, then simply add `from updater import check_update` to your code (if in python), and then run the `check_update()` function somewhere in your code.

If you selected `updater_w_config`, then change the default config to suit your needs with keys etc.
