import os
import cv2
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-f", type=str, default=None, required=True,
                    help="输入同级目录下图片的名称")
args  = parser.parse_args()


file_path = os.path.abspath(args.f) 

img = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)
assert img.shape[-1] == 3

size = os.path.getsize(file_path)
row, col = img.shape[:2]
width = (size - 53) // 3 // row
height = (size - 53) // 3 // col

print(f"宽度可能为: {width}")
print(f"高度可能为: {height}")

with open(file_path, "rb") as f:
    data = f.read()

with open("width.bmp", "wb") as f:
    f.write(data[:0x12] + width.to_bytes(4, byteorder="little", signed=False) + data[0x16:])

with open("height.bmp", "wb") as f:
    f.write(data[:0x16] + height.to_bytes(4, byteorder="little", signed=False) + data[0x1a:])

