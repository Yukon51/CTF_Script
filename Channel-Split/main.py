import os
import cv2
import shutil
import argparse
import itertools
import numpy as np
from PIL import Image


parser = argparse.ArgumentParser()
parser.add_argument('-f', type=str, default=1,
                    help='图片路径')
parser.add_argument('-size', type=int, default=1,
                    help='图片放大倍数(默认1倍) 待开发')
parser.add_argument('-inversion', nargs='?', const=True, default=False,
                    help='是否图片反色(默认关闭)')
args = parser.parse_args()
# INTER_NEAREST

file_path = os.path.abspath(args.f)
file_name = os.path.splitext(file_path)[0].split("\\")[-1]
save_path = os.path.join(os.path.dirname(file_path), file_name)


def get_channel_dic(shape):
    try:
        if shape[2] == 3:
            channel_dic = ["Blue", "Green", "Red"]
        elif shape[2] == 4:
            channel_dic = ["Alpha", "Blue", "Green", "Red"]
    except IndexError:
        return ["Gray"]
    return channel_dic

def split_channel_bit(img, height, width):
    '''
    分离图片通道，依次8bit分离
    '''
    np_bit = [[int(i) for i in bin(img[y, x])[2:].zfill(8)] for y, x in itertools.product(range(height), range(width))]
    np_bit = np.array(np_bit)
    np_bit = np.where(np_bit == 0, 0, 255) # 如果为0就是0黑色，如果为1就为255白色
    np_bit.astype(np.uint8) # 类型转换
    return np_bit

def colour_inversion(img):
    return 255 ^ img

if __name__ == '__main__':
    # delete target and makedirs
    if os.path.exists(save_path):
        shutil.rmtree(save_path)
    os.makedirs(save_path)

    # read img
    img = Image.open(file_path)
    img = np.array(img, np.uint8)[:,:,::-1]
    # img = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)
    height, width = img.shape[:2]
    print(img.shape)

    # image inversion
    if args.inversion:
        save_img = colour_inversion(img)
        save_img = Image.fromarray(save_img)
        save_img.save(os.path.join(save_path, "Colour Inversion.png"))

    # split channel
    channel_dic = get_channel_dic(img.shape)
    for channel, channel_str in enumerate(channel_dic):
        channel_img = img[:, :] if len(channel_dic) == 1 else img[:, :, channel]
        np_bit = split_channel_bit(channel_img, height, width)
        for i in range(8):
            save_img = np_bit[:, 7-i].reshape(height, width).astype(np.uint8)
            save_img = Image.fromarray(save_img, "L")
            save_img.save(os.path.join(save_path, f"{channel_str} plane {i}.png"))