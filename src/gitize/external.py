import json
from pathlib import Path
import subprocess
from urllib.request import urlopen
from prj_gen.userinput import get_choices_from_list
from requests_cache import CachedSession

KEY = "key"

# Grab license from github
def get_license(path): 
    session = CachedSession()
    response = session.get('https://api.github.com/licenses')
    lics = response.json()
    if len(lics) < 1:
        return
    names = []
    urls = []  
    for i in lics:
        names.append(i["name"])
        urls.append(i["url"])
    i_lic = get_choices_from_list(key="License", ch=names, df=0, pr="License")
    with urlopen(urls[i_lic[KEY]]) as url:
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
