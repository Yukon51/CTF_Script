import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', type=str, default=None, required=True,
                    help='输入10进制数据')
args  = parser.parse_args()


data = args.t
ret = ""
while len(data):
    if int(data[:3]) <= 127:
        ret += chr(int(data[:3]))
        data = data[3:]
    else:
        ret += chr(int(data[:2]))
        data = data[2:]
print(ret)