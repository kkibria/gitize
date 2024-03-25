from pathlib import Path
from warnings import warn
from . import get_template_path, set_warnigs_hook
from .hook import MyGen
import argparse

def build(dstpath, params):
    dst = Path(dstpath)
    if not params["force"]:
        if dst.exists():
            warn(f'"{dstpath}" already exists, use --force, exiting!')
            return
    g = MyGen(get_template_path())
    g.update_params(params)
    g.run(dst)

def main():
    params = {"app": "gitize"}

    parser = argparse.ArgumentParser(
        prog=params["app"],
        description='Creates a git initialized poetry project',
        epilog=f'python -m {params["app"]}')

    parser.add_argument('path')
    parser.add_argument('-f', '--force', default=False,
                    action='store_true')
    
    args = parser.parse_args()
    params["force"] = args.force

    set_warnigs_hook()
    try:
        build(args.path, params)
    except Exception as e:
        print(f'{e.__class__.__name__}:', *e.args)
        return 1
    
    return 0