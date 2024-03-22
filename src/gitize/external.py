import json
from pathlib import Path
import subprocess
from urllib.request import urlopen
from prj_gen.userinput import get_choices_from_dict
from requests_cache import CachedSession

# Grab license from github
def get_license(path): 
    KEY = "key"
    session = CachedSession()
    response = session.get('https://api.github.com/licenses')
    lics = response.json()
    if len(lics) < 1:
        return
    n = 1
    ch = {}
    urls = {}  
    for i in lics:
        key = f'{n}'
        n += 1
        ch[key] = i["name"]
        urls[key] = i["url"]
    r = get_choices_from_dict(key="License", ch=ch, df="1", pr="License")
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
    print(f'===> running "{" ".join(extcmd)}"')
    sts = subprocess.run(extcmd) 
