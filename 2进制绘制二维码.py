import cv2
import argparse
import itertools
import numpy as np


parser = argparse.ArgumentParser()
parser.add_argument('-f', type=str, default=None, required=True,
                    help='输入文件名称')
parser.add_argument('-r', type=int, default=None, required=True,
                    help='输入行数',)
parser.add_argument('-c', type=int, default=None, required=True,
                    help='输入列数')
parser.add_argument('-size', type=int, default=15,
                    help='图片放大倍数(默认15倍)')
args = parser.parse_args()

file_name = args.f
row, col = args.r, args.c
size = args.size

# read file
with open(file_name, "r") as f:
    data = f.read()

img1 = np.zeros((row * size, col * size, 3))
img2 = np.zeros((row * size, col * size, 3))

left_top_point = []
for i, j in itertools.product(range(0, row * size, size), range(0, col * size, size)):
    left_top = (j, i)
    left_top_point.append(left_top)

def draw_QR(img, reverse=False):
    for i, v in enumerate(data[:row*col]):
        right_bottom_point = (
            left_top_point[i][0] + size, left_top_point[i][1] + size)
        if not reverse:
            cv2.rectangle(img, left_top_point[i], right_bottom_point, color=(
                255, 255, 255), thickness=-1) if v == "0" else cv2.rectangle(img, left_top_point[i], right_bottom_point, color=(0, 0, 0), thickness=-1)
        else:
            cv2.rectangle(img, left_top_point[i], right_bottom_point, color=(0, 0, 0), thickness=-1) if v == "0" else cv2.rectangle(
                img, left_top_point[i], right_bottom_point, color=(255, 255, 255), thickness=-1)

draw_QR(img1, reverse=False)
draw_QR(img2, reverse=True)

# 添加白色边框
img1 = cv2.copyMakeBorder(img1, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=(139, 139, 0))
img2 = cv2.copyMakeBorder(img2, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=(139, 139, 0))

# 水平拼接
img = np.concatenate([img1, img2], axis=1)

cv2.imshow("images", img)
cv2.waitKey(0)