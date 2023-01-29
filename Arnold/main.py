import os
import cv2
import argparse
import numpy as np
from PIL import Image


parser = argparse.ArgumentParser()
parser.add_argument('-t', type=str, default=None, required=True, choices=["encode", "decode"],
                    help='encode | decode')
parser.add_argument('-f', type=str, default=None, required=True,
                    help='输入文件名称')
parser.add_argument('-n', type=int, default=1, required=False,
                    help='输入参数n')
parser.add_argument('-a', type=int, default=None, required=True,
                    help='输入参数a')
parser.add_argument('-b', type=int, default=None, required=True,
                    help='输入参数b')
args  = parser.parse_args()


# def arnold(img, n, a, b):
#     new_img = np.zeros((r, c, 3), np.uint8)

#     for _ in range(n):
#         for i in range(r):
#             for j in range(c):
#                 x = (i + b * j) % r
#                 y = (a * i + (a * b + 1) * j) % c
#                 new_img[x, y] = img[i, j]
#         img = np.copy(new_img)
#     return new_img

# def dearnold(img, n, a, b):
#     new_img = np.zeros((r, c, 3), np.uint8)

#     for _ in range(n):
#         for i in range(r):
#             for j in range(c):
#                 x = ((a * b + 1) * i - b * j) % r
#                 y = (-a * i + j) % c
#                 new_img[x, y] = img[i, j]
#         img = np.copy(new_img)
#     return new_img

def arnold(img, n, a, b):
    new_img = np.zeros((r, c, 3), np.uint8)

    for _ in range(n):
        y, x = np.meshgrid(np.arange(c), np.arange(r))
        new_x = (x + b * y) % r
        new_y = (a * x + (a * b + 1) * y) % c
        new_img[new_x, new_y] = img
        img = np.copy(new_img)
    return new_img

def dearnold(img, n, a, b):
    new_img = np.zeros((r, c, 3), np.uint8)

    for _ in range(n):
        y, x = np.meshgrid(np.arange(c), np.arange(r))
        new_x = ((a * b + 1) * x - b * y) % r
        new_y = (-a * x + y) % c
        new_img[new_x, new_y] = img
        img = np.copy(new_img)
    return new_img


if __name__ == '__main__':
    img_path = os.path.abspath(args.f)
    file_name = os.path.splitext(img_path)[0].split("\\")[-1]
    img = np.array(Image.open(img_path).convert("RGB"), np.uint8)[:,:,::-1]
    r, c = img.shape[:2]
    n, a, b = args.n, args.a, args.b

    if args.t == "encode":
        new_img = arnold(img, n, a, b)

        # b = 0
        # for a in range(300, 303):
        #     new_img = arnold(img, n, a, b)
        #     cv2.imwrite(f"./out_r/{file_name}_{n}_{a}_{b}.png", new_img)
        # exit()
    elif args.t == "decode":
        new_img = dearnold(img, n, a, b)

        # a = 301
        # for b in range(368, 378):
        #     new_img = dearnold(img, n, a, b)
        #     cv2.imwrite(f"./out_r/{file_name}_{n}_{a}_{b}.png", new_img)
        # exit()

    cv2.imwrite(f"./{file_name}_{n}_{a}_{b}.png", new_img)
