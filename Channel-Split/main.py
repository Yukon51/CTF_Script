import os
import cv2
import argparse
import itertools
import numpy as np
from tqdm import tqdm
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument('-size', type=int, default=1,
                    help='图片放大倍数(默认1倍)')
args = parser.parse_args()
# INTER_NEAREST

base_dir = os.path.dirname(os.path.abspath(__file__))
source_path, target_path = os.path.join(base_dir, "source"), os.path.join(base_dir, "target")


def img_rename(path, index):
    file_tail = os.path.splitext(file_name)[-1] # 从后往前遍历，文件尾部在后面，可以节省遍历次数
    rename_path = os.path.join(source_path, f"{index}{file_tail}")
    os.rename(path, rename_path)
    return rename_path
    
def makedir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def split_img(img):
    '''
    分离图片通道，依次8bit分离
    '''
    np_bit = [[int(i) for i in bin(img.getpixel((x, y)))[2:].zfill(8)] for y, x in itertools.product(range(img.height), range(img.width))]
    np_bit = np.array(np_bit)
    # 如果为0就是0黑色，如果为1就为255白色
    np_bit = np.where(np_bit == 0, 0, 255)
    np_bit.astype(np.uint8) # 类型转换
    return np_bit

with tqdm(enumerate(os.listdir(source_path)), desc="Channel Split") as bar:
    for index, file_name in bar:
        # rename img name
        img_path = os.path.join(source_path, f"{file_name}")
        rename_path = img_rename(img_path, index)

        # create target dirs
        save_path = os.path.join(target_path, f"{index}")
        makedir(save_path)

        img = Image.open(rename_path)
        height, width =  img.size
        for channel in img.getbands():
            np_bit = split_img(img.getchannel(channel))
            for i in range(8):
                cv2.imwrite(os.path.join(save_path, f"{channel}{i}.png"), np_bit[:, 7-i].reshape(width, height, 1))
