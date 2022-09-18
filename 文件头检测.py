import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-f", type=str, default=None, required=True,
                    help="输入同级目录下文件的名称")
args  = parser.parse_args()

file_head = {
    "FFD8FF": "JPG",
    "89504E47": "PNG",
    "47494638": "GIF",
    "504B0304": "ZIP",
    "424D": "BMP",
    "52617221": "RAR",
    "57415645": "WAV",
    "41564920": "AVI",
    "377ABCAF271C": "7Z",
    "425047": "BPG",
    "7F454C46": "ELF",
    "03F30D0A": "PYC",
    "52494646": "WEBP",
    "8004": "Python-Pickle",
    "????????66747970": "MP4/M4A/MOV/3GP",
}

with open(args.f, "rb") as f:
    data = f.read()

# xor异或
flag = 0
for head, value in file_head.items():
    xor_ret = [int(head[j:j+2], 16) ^ data[i] for i, j in enumerate(range(0, len(head), 2)) if head[j:j+2] != "??"]

    if all(item == xor_ret[0] for item in xor_ret):
        flag = 1
        print(f"文件可能是: {value} 格式, Xor数值: {hex(xor_ret[0])}")

if not flag:
    print("没有异或到符合的文件头!")

# not取反
not_data = b""
for i in range(len(max(list(file_head.keys()), key=lambda x: len(x))) // 2): # 取最长的head_file的头除以二即可
    not_data += ((256 - data[i]) % 256).to_bytes(1, byteorder="big", signed=False)

flag = 0
for head, value in file_head.items():
    ret = []
    for i, j in enumerate(range(0, len(head), 2)):
        if head[j:j+2] == "??":
            ret.append(True)
        elif int(head[j:j+2], 16) == not_data[i]:
            ret.append(True)
        else:
            ret.append(False)

    if all(ret):
        flag = 1
        print(f"文件可能是: {value} 格式, 取反后即可得到!")

if not flag:
    print("取反没有得到符合的文件头!")

os.system("pause")