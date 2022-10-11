import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-f", type=str, default=None, required=True,
                    help="输入同级目录下文件的名称")
parser.add_argument('-pro', nargs='?', const=True, default=False,
                        help='(default: False)')
args  = parser.parse_args()

file_dir = args.f
file_name = file_dir.split("\\")[-1]

with open(file_dir, "rb") as fi, open(f"reverse_{file_name}", "wb") as fo:
    data = fi.read()[::-1]
    if args.pro:
        for i in data:
            fo.write((((i >> 4) & 0xf) | ((i << 4) & 0xf0)).to_bytes(1, byteorder="big", signed=False))
    else:
        fo.write(data)
