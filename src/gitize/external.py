import subprocess

def cmds(path):
    return {
        "poetry" : f'poetry new --src {path}'.split(),
        "git" : f'git init {path}'.split(),
        "user": f'git config user.name'.split(),
        "email": f'git config user.email'.split(),
    }

def run_cmd(cmd, path):
    extcmd = cmds(path)[cmd]
    print(f'===> running "{" ".join(extcmd)}"')
    sts = subprocess.run(extcmd, stdout=subprocess.PIPE)
    return sts.stdout.decode('utf-8').strip()