import re
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-f", type=str, default=None, required=True,
                    help="输入同级目录下文件的名称")
args  = parser.parse_args()

with open(args.f, "rb") as f:
    data = f.read()
data = data.decode("latin1")

# re.IGNORECASE 忽略大小写
re_relu = ["(key.*?) ", "(flag.*?) ", "(ctf.*?) "]
for re_str in re_relu:
    ret = re.findall(re_str, data, re.IGNORECASE)
    if ret != []:
        print(ret)