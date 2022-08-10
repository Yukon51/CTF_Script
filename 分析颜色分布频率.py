# 在线网站可视化的效果更好：https://www.qtool.net/colour
import argparse
import itertools
from PIL import Image


parser = argparse.ArgumentParser()
parser.add_argument('-f', type=str, default=None, required=True,
                    help='输入文件名称')
args  = parser.parse_args()

img = Image.open(args.f)

dict_ = {}
for y, x in itertools.product(range(img.height), range(img.width)):
    color = img.getpixel((x, y))
    if dict_.get(color, None):
        dict_[color] += 1
    else:
        dict_[color] = 1
# sorted 可要可不要
dict_ = sorted(dict_.items(), key=lambda x:x[1], reverse=False)

# 筛选出出现次数大于5次的颜色并打印
for color, count in dict_:
    if count > 5:
        print((color, count))