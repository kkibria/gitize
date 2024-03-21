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
        description='What the program does',
        epilog='Text at the bottom of help')

    parser.add_argument('path')           # positional argument
    # parser.add_argument('-c', '--count')      # option that takes a value
    # parser.add_argument('-v', '--verbose',
    #     action='store_true')  # on/off flag
    
    args = parser.parse_args()
    # print(args.filename, args.count, args.verbose)
    build(args.path)
