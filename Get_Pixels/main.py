import os
import re
import cv2
import argparse
import itertools
import numpy as np


parser = argparse.ArgumentParser()
parser.add_argument('-f', type=str, default=None, required=True,
                    help='输入文件名称')
parser.add_argument('-p', type=str, default=None, required=True,
                    help='输入左上顶点和右下顶点坐标 (如:220x344+3520x2150)')
parser.add_argument('-n', type=str, default=None, required=True,
                    help='输入宽度间隔和高度间隔 (如:44x86)')
args  = parser.parse_args()

if __name__ == '__main__':
    if re.search(r"^\d{1,}x\d{1,}\+\d{1,}x\d{1,}$", args.p) and re.search(r"^\d{1,}x\d{1,}$", args.n):
        x1, y1 = map(lambda x: int(x), args.p.split("+")[0].split("x"))
        x2, y2 = map(lambda x: int(x), args.p.split("+")[1].split("x"))
        width, height = map(lambda x: int(x), args.n.split("x"))

        img_path = os.path.abspath(args.f)
        file_name = img_path.split("\\")[-1]

        img = cv2.imread(img_path, cv2.IMREAD_COLOR)
        row, col = img.shape[:2]

        r, c = len(range(y1, y2 + 1, height)), len(range(x1, x2 + 1, width))
        new_img = np.zeros(shape=(r, c, 3))
        for y, x in itertools.product(range(r), range(c)):
            new_img[y, x] = img[y1 + y * height, x1 + x * width]

        cv2.imwrite(f"_{file_name}", new_img)
        print("已保存到运行目录中...")
    else:
        print("参数-p或参数-n, 输入错误!")