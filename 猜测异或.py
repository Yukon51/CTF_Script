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
    "8004": "Python-Pickle"
}

with open(args.f, "rb") as f:
    data = f.read()

flag = 0
for head, value in file_head.items():
    xor_ret = [int(head[k * 2 : k * 2 + 2], 16) ^ data[i] for i, k in enumerate(range(len(head) // 2))]

    if all(item == xor_ret[0] for item in xor_ret):
        flag = 1
        print(f"文件可能是: {value} 格式, Xor数值: {hex(xor_ret[0])}")

if not flag:
    print("没有异或到符合的文件头!")