import os
import argparse
import numpy as np
import matplotlib.pyplot as plt


parser = argparse.ArgumentParser()
parser.add_argument("-f", type=str, default="out.txt", required=False,
                    help="输入同级目录下图片的名称")
args  = parser.parse_args()

TITLE = ["LEFT", "RIGHT", "ALL", "MOVE_LEFT", "MOVE_RIGHT", "MOVE_ALL"]
FILE_PATH = os.path.abspath(args.f)

def read_file():
    with open(FILE_PATH, "r") as f:
        data = f.read().splitlines()
    return data

def get_pos():
    data = read_file()

    posx, posy = 0, 0
    pos_left, pos_right, pos_all = [], [], []
    for line in data:
        x, y = int(line[2:4], 16), int(line[5:7], 16)
        if x > 127:
            x -= 256
        if y > 115:
            y -= 256
        posx += x
        posy += y
        # 1 for left , 2 for right , 0 for nothing
        btn_flag = int(line[:2], 16)
        if btn_flag == 1:  # 1 代表左键，2代表右键
            pos_left.append((posx, -posy))
            pos_all.append((posx, -posy))
        elif btn_flag == 2:
            pos_right.append((posx, -posy))
            pos_all.append((posx, -posy))
    return [np.array(pos_left), np.array(pos_right), np.array(pos_all)]

def plot_point(arr, axes, move=False):
    if arr.size != 0:
        axes.plot(arr[:, 0], arr[:, 1]) if move else axes.scatter(arr[:, 0], arr[:, 1], s=10, marker="x")

if __name__ == '__main__':
    all_pos = get_pos()

    _, axes = plt.subplots(2, 3, figsize=(15, 8))
    for i in range(len(axes)):
        for j in range(len(axes[i])):
            ax = axes[i][j]
            count = i * 3 + j
            ax.set_title(TITLE[count])
            if count < 3:
                plot_point(all_pos[count%3], ax)
            else:
                plot_point(all_pos[count%3], ax, move=True)

    plt.tight_layout()
    plt.show()
