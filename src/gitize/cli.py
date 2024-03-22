from pathlib import Path
from .hook import MyGen
import argparse

def build(dstpath):
    dst = Path(dstpath)
    if dst.exists():
        print(f'Note: {dstpath} already exists, exiting!')
        return
    g = MyGen("template")
    g.update_params({"path": dstpath})
    g.run(dst)

def main():
    parser = argparse.ArgumentParser(
        prog='gitize',
        description='creates a git initialized poetry project',
        epilog='python -m gitize')

    parser.add_argument('path')
    
    args = parser.parse_args()
    build(args.path)
