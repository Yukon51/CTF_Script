import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-t', type=str, default=None, required=True,
                    help='输入十六进制文本')
args  = parser.parse_args()


def range_N(isPositiveInteger=None):
    for i in range(256):
        try:
            flag = "".join(chr(int(j, 16) + i) for j in one_byte) if isPositiveInteger else "".join(chr(int(j, 16) - i) for j in one_byte)
            print(f"[ +{i} ] --> {flag}") if isPositiveInteger else print(f"[ -{i} ] --> {flag}")
        except ValueError:
            print(f"[ 最多只能加到{i - 1}! ]\n") if isPositiveInteger else print(f"[ 最多只能减到{i - 1}! ]\n")
            break


one_byte = [args.t[i: i + 2] for i in range(0, len(args.t), 2)]
flag = "".join(chr(int(i, 16)) for i in one_byte)
print(f"\n[ 16进制 -> Ascii ]:\n{flag}\n")

input_ = input("转换为10进制然后 - N, (N范围0~255)? (Y/n):")
if input_ not in ["Y", "y", ""]:
    exit()
else:
    range_N(isPositiveInteger=False)

input_ = input("转换为10进制然后 + N, (N范围0~255)? (Y/n):")
if input_ not in ["Y", "y", ""]:
    exit()
else:
    range_N(isPositiveInteger=True)