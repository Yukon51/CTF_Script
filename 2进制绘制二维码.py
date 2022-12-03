import os
import cv2
import time
import argparse
import itertools
import numpy as np


parser = argparse.ArgumentParser()
parser.add_argument('-f', type=str, default=None, required=True,
                    help='输入文件名称')
parser.add_argument('-size', type=int, default=5,
                    help='图片放大倍数(默认5倍)')
args = parser.parse_args()

file_path = os.path.join(args.f)

if not os.path.exists("./out"):
    os.mkdir("./out")

# read binary txt
with open(file_path, "r") as f:
    data = f.read().strip()

def draw_QR(img, reverse=False):
    for i, v in enumerate(data[:row*col]):
        right_bottom_point = (left_top_point[i][0] + size, left_top_point[i][1] + size)
        if not reverse:
            cv2.rectangle(img, left_top_point[i], right_bottom_point, color=(
                255, 255, 255), thickness=-1) if v == "0" else cv2.rectangle(img, left_top_point[i], right_bottom_point, color=(0, 0, 0), thickness=-1)
        else:
            cv2.rectangle(img, left_top_point[i], right_bottom_point, color=(0, 0, 0), thickness=-1) if v == "0" else cv2.rectangle(
                img, left_top_point[i], right_bottom_point, color=(255, 255, 255), thickness=-1)
    return img

if __name__ == '__main__':
    # 计算宽高
    dic = {X: int(len(data) / X) for X in range(1, len(data)) if len(data) % X == 0}
    size = args.size

    for row, col in dic.items():
        img1, img2 = np.zeros((row * size, col * size, 1)), np.zeros((row * size, col * size, 1))

        left_top_point = []
        for i, j in itertools.product(range(0, row * size, size), range(0, col * size, size)):
            left_top = (j, i)
            left_top_point.append(left_top)

        cv2.imwrite(f"./out/{col}_{row}.png", draw_QR(img1, reverse=False))
        cv2.imwrite(f"./out/{col}_{row}_reverse.png", draw_QR(img2, reverse=True))
        print(f"[-] 宽度:{col:6} 高度:{row:6}, 已保存在运行目录out中...")
    print("[-] 已经遍历完所有情况, 即将自动关闭!")
    time.sleep(0.5)
