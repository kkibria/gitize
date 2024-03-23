from pathlib import Path
from warnings import warn
from .hook import MyGen
import argparse

def build(dstpath):
    dst = Path(dstpath)
    if dst.exists():
        warn(f'{dstpath} already exists, exiting!')
        return
    g = MyGen("template")
    g.run(dst)

def main():
    parser = argparse.ArgumentParser(
        prog='gitize',
        description='creates a git initialized poetry project',
        epilog='python -m gitize')

    parser.add_argument('path')
    
    args = parser.parse_args()
    try:
        build(args.path)
    except Exception as e:
        print(f'{e.__class__.__name__}:', *e.args)
        return 1
    
    return 0 