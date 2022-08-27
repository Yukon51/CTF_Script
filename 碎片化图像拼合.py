import os
import cv2
import numpy as np


channel = 2 # bgr三通道
imgs = [cv2.imread(os.path.join("./images", i)) for i in os.listdir("./images")]

def get_diff(A: np.array, B: np.array):
    # return sum((A[:, -1, channel] - B[:, 0, channel]))
    return sum((A[:, -1, channel] - B[:, 0, channel]) ** 0.25)

def combine(img1, img2):
    return np.concatenate([img1, img2], axis=1)

while len(imgs) > 1:
    index = None
    min_diff = None
    for j in range(1, len(imgs)):
        if min_diff is None:
            min_diff = get_diff(imgs[0], imgs[j])
            index = j
        elif (diff := get_diff(imgs[0], imgs[j])) < min_diff:
            min_diff = diff
            index = j

    imgs[0] = combine(imgs[0], imgs[index])
    imgs.pop(index)

cv2.imwrite("flag.png", imgs[0])