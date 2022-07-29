import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-t', type=str, default=None, required=True,
                    help='输入二进制文本')
args  = parser.parse_args()

cipher = args.t

def BintoAsc(cipher):
    print(cipher)
    # 7bit 一字节
    print("[7Bit]: " + "".join(chr(int(cipher[i:i+7], 2)) for i in range(0, len(cipher), 7)))
    # 8bit 一字节
    print("[8Bit]: " + "".join(chr(int(cipher[i:i+8], 2)) for i in range(0, len(cipher), 8)))
    print()

def Reverse_BintoAsc(cipher):
    # 7bit 一字节
    print("[7Bit]: " + "".join(chr(int(cipher[i:i+7][::-1], 2)) for i in range(0, len(cipher), 7)))
    # 8bit 一字节
    print("[8Bit]: " + "".join(chr(int(cipher[i:i+8][::-1], 2)) for i in range(0, len(cipher), 8)))
    print()

# 正常情况
BintoAsc(cipher)

# 特殊情况1
input_ = input("是否尝试全部字节倒序后转换Ascii码? (Y/n):")
if input_ not in ["Y", "y", ""]:
    exit()
else:
    reverse_cipher = cipher[::-1]
    BintoAsc(reverse_cipher)
# 特殊情况2

input_ = input("是否尝试每个字节依次倒序后转换Ascii码? (Y/n):")
if input_ not in ["Y", "y", ""]:
    exit()
else:
    Reverse_BintoAsc(cipher)

# 特殊情况3
input_ = input("是否尝试0和1交换后转换Ascii码? (Y/n):")
if input_ not in ["Y", "y", ""]:
    exit()
else:
    new_cipher = "".join("1" if i == "0" else "0" for i in cipher)
    BintoAsc(new_cipher)