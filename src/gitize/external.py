import subprocess
from urllib.request import urlopen

def get_licenses(): 
    return urlopen('https://api.github.com/licenses').read()

def cmds(path):
    return {
        "poetry" : f'poetry new --src {path}'.split(),
        "git" : f'git init {path}'.split(),
    }

def run_cmd(cmd, path):
    extcmd = cmds(path)[cmd]
    print(f'running "{" ".join(extcmd)}"')
    sts = subprocess.run(extcmd) 

if __name__ == '__main__':
    cmd = cmds("../gitize2")
    print(cmd["poetry"], cmd["git"])