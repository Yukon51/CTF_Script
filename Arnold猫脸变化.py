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

if __name__ == '__main__':
    img_path = os.path.abspath(args.f)
    file_name = img_path.split("\\")[-1]
    img = cv2.imread(img_path, cv2.IMREAD_COLOR)
    r, c = img.shape[:2]
    a, b = args.a, args.b

    if r == c:
        if args.t == "encode":
            new_img = arnold(img, a, b)
        elif args.t == "decode":
            new_img = dearnold(img, a, b)
    else:
        print("[-] 图片宽高不一致, 无法进行猫脸变化!")

    cv2.imwrite(f"./Arnold_{a}_{b}_{file_name}", new_img)
