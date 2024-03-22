import json
from pathlib import Path
import subprocess
from urllib.request import urlopen
from prj_gen.userinput import get_choices_from_dict

def get_license(path): 
    KEY = "key"
    with urlopen('https://api.github.com/licenses') as url:
        lics = json.load(url)
    ch = {}
    urls = {}  
    for i in lics:
        key = i[KEY]
        ch[key] = i["name"]
        urls[key] = i["url"]
    r = get_choices_from_dict(key="licenses", ch=ch, df=lics[0][KEY], pr="licenses")
    with urlopen(urls[r[KEY]]) as url:
        lic = json.load(url)
    dst = Path(path).joinpath("LICENSE.txt")
    with dst.open("w") as f:
        f.write(lic["body"])

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