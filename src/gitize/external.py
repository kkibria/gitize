import subprocess

def cmds(path):
    return {
        "poetry" : f'poetry new --src {path}'.split(),
        "git" : f'git init {path}'.split(),
    }

def run_cmd(cmd, path):
    extcmd = cmds(path)[cmd]
    print(f'===> running "{" ".join(extcmd)}"')
    sts = subprocess.run(extcmd) 
