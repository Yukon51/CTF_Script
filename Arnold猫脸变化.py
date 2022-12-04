import os
import cv2
import argparse
import numpy as np


parser = argparse.ArgumentParser()
parser.add_argument('-t', type=str, default=None, required=True, choices=["encode", "decode"],
                    help='encode | decode')
parser.add_argument('-f', type=str, default=None, required=True,
                    help='输入文件名称')                  
parser.add_argument('-a', type=int, default=None, required=True,
                    help='输入参数a')
parser.add_argument('-b', type=int, default=None, required=True,
                    help='输入参数b')
args  = parser.parse_args()


def arnold(img, a, b):
    p = np.zeros((r, c, 3), np.uint8)
    for i in range(r):
        for j in range(c):
            x = (i + b * j) % r
            y = (a * i + (a * b + 1) * j) % c
            p[x, y] = img[i, j]
    return p

def dearnold(img, a, b):
    p = np.zeros((r, c, 3), np.uint8)
    for i in range(r):
        for j in range(c):
            x = ((a * b + 1) * i - b * j) % r
            y = (-a * i + j) % c
            p[x, y] = img[i, j]
    return p

file_name = os.path.abspath(args.f).split("\\")[-1]
img = cv2.imread(args.f, cv2.IMREAD_COLOR)
r, c = img.shape[:2]

if r == c:
    if args.t == "encode":
        img = arnold(img, a=args.a, b=args.b)
    elif args.t == "decode":
        img = dearnold(img, a=args.a, b=args.b)
else:
    print("[-] 图片宽高不一致, 无法进行猫脸变化!")

cv2.imwrite(f"Arnold_{file_name}", img)
