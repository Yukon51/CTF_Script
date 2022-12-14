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
                    help='输入左上顶点和右下顶点坐标 (如:-p 220x344+3520x2150)')
parser.add_argument('-n', type=str, default=None, required=True,
                    help='输入宽度间隔和高度间隔 (如:-n 44x86)')
parser.add_argument('-size', type=str, default='1x1', required=False,
                    help='输入截取图像的大小 (如:-size 7x7)')
parser.add_argument('-resize', type=int, default=1, required=False,
                    help='输入截取图像放大倍数 (如:-resize 1)')
args  = parser.parse_args()

if __name__ == '__main__':
    if re.search(r"^\d{1,}x\d{1,}\+\d{1,}x\d{1,}$", args.p) and re.search(r"^\d{1,}x\d{1,}$", args.n) and re.search(r"^\d{1,}x\d{1,}$", args.size):
        x1, y1 = map(lambda x: int(x), args.p.split("+")[0].split("x"))
        x2, y2 = map(lambda x: int(x), args.p.split("+")[1].split("x"))
        width, height = map(lambda x: int(x), args.n.split("x"))
        width_size, height_size = map(lambda x: int(x), args.size.split("x"))

        img_path = os.path.abspath(args.f)
        file_name = img_path.split("\\")[-1]

        img = cv2.imread(img_path, cv2.IMREAD_COLOR)
        row, col = img.shape[:2]

        r, c = len(range(y1, y2 + 1, height)), len(range(x1, x2 + 1, width))
        new_img = np.zeros(shape=(r * height_size * args.resize, c * width_size * args.resize, 3))
        for y, x in itertools.product(range(r), range(c)):
            for y_size in range(height_size):
                for x_size in range(width_size):
                    # new_img[y * height_size + y_size, x * width_size + x_size] = img[y1 + y * height + y_size, x1 + x * width + x_size]
                    pt1 = ((x * width_size + x_size) * args.resize, (y * height_size + y_size) * args.resize)
                    pt2 = ((x * width_size + x_size) * args.resize + args.resize, (y * height_size + y_size) * args.resize + args.resize)
                    color = img[y1 + y * height + y_size, x1 + x * width + x_size].tolist()
                    cv2.rectangle(new_img, pt1=pt1, pt2=pt2, color=color, thickness=-1)
            

        cv2.imwrite(f"_{file_name}", new_img)
        print("已保存到运行目录中...")
    else:
        print("参数-p或参数-n或参数-size, 输入错误!")