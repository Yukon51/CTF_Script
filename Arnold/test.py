import cv2
import itertools
import numpy as np

def g_xy(x, y):
    yield from np.c_[x, y]

def arnold(img, a, b):
    r, c = img.shape[:2]
    new_img = np.zeros((r, c, 3), np.uint8)
    arr = np.array([[1, a], [b, a*b + 1]])
    lis = np.array([[y, x] for y, x in itertools.product(range(r), range(c))])
    out = np.matmul(lis, arr)
    x = out[:, 0] % r
    y = out[:, 1] % c

    g = g_xy(x, y)

    for i in range(r):
        for j in range(c):
            x, y = next(g)
            new_img[x, y] = img[i, j]
    return new_img

def dearnold(img, a, b):
    r, c = img.shape[:2]
    new_img = np.zeros((r, c, 3), np.uint8)
    arr = np.array([[a*b + 1, -a], [-b, 1]])
    lis = np.array([[y, x] for y, x in itertools.product(range(r), range(c))])
    out = np.matmul(lis, arr)
    x = out[:, 0] % r
    y = out[:, 1] % c

    p = np.c_[x, y]

    g = g_xy(x, y)

    for i in range(r):
        for j in range(c):
            x, y = next(g)
            new_img[x, y] = img[i, j]
    return new_img


if __name__ == '__main__':
    a, b = 1, 1
    img = cv2.imread("./test.png")
    cv2.imwrite("encode.png", arnold(img, a, b))

    img = cv2.imread("./encode.png")
    cv2.imwrite("decode.png", dearnold(img, a, b))

