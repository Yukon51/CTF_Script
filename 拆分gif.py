import os
import argparse
from tqdm import tqdm
from PIL import Image

process_py = '''import itertools
from PIL import Image


bin_str = ""
for num in range():
    img_path = f"./images/{num}.png"
    img = Image.open(img_path)

    # 列优先
    for y, x in itertools.product(range(img.height), range(img.width)):
        colors = img.getpixel((x, y))
        ...

    # 行优先
    for x, y in itertools.product(range(img.width), range(img.height)):
        colors = img.getpixel((x, y))
        ...

print(bin_str)'''


parser = argparse.ArgumentParser()
parser.add_argument("-f", type=str, default=None, required=True,
                    help="输入同级目录下文件的名称")
args  = parser.parse_args()


save_path = "./output"
py_save_path = os.path.join(save_path, "Example.py")
img_save_path = os.path.join(save_path, "./images")

if not os.path.exists(os.path.join(img_save_path)):
    os.makedirs(os.path.join(img_save_path))

img = Image.open(args.f)
n_frames = img.n_frames
# 保存处理脚本
process_py = process_py.replace("帧数", str(n_frames))
with open(py_save_path, "w") as f:
    f.write(process_py)

# 保存每一帧图片

with tqdm(range(n_frames), desc="Save Image") as num_bar:
    for i in num_bar:
        img.seek(i)
        img.save(os.path.join(img_save_path, f"{i}.png"))
print("拆分GIF成功，并自动帮您保存了处理脚本!")