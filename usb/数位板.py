import os
import argparse
import matplotlib.pyplot as plt


parser = argparse.ArgumentParser()
parser.add_argument("-f", type=str, default="out.txt", required=False,
                    help="输入同级目录下的名称")
args  = parser.parse_args()

FILE_PATH = os.path.abspath(args.f)

data = []
with open(FILE_PATH, "r") as f:
    data.extend(line for line in f if line[16:18] != "00")
    
X, Y = [], []
for line in data:
    x0 = int(line[4:6], 16)
    x1 = int(line[6:8], 16)
    x = x0 + x1 * 256
    y0 = int(line[10:12], 16)
    y1 = int(line[12:14], 16)
    y = y0 + y1 * 256
    X.append(x), Y.append(-y)

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_title("result")
ax1.scatter(X, Y, c='b', marker='x')
plt.show()
