from pathlib import Path
from warnings import warn
from .hook import MyGen
import argparse

def build(dstpath, params):
    dst = Path(dstpath)
    if dst.exists():
        warn(f'{dstpath} already exists, exiting!')
        return
    g = MyGen("template")
    g.update_params(params)
    g.run(dst)

def main():
    params = {"app": __name__.split(".")[0]}

    parser = argparse.ArgumentParser(
        prog=params["app"],
        description='creates a git initialized poetry project',
        epilog=f'python -m {params["app"]}')

    parser.add_argument('path')
    
    args = parser.parse_args()
    try:
        build(args.path, params)
    except Exception as e:
        print(f'{e.__class__.__name__}:', *e.args)
        return 1
    
    return 0