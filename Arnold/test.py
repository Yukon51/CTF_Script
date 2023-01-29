from PIL import Image
import numpy as np

def arnold(im_file, a, b):
    img = np.array(Image.open(im_file))
    height, width, color = img.shape
    res_img = np.zeros((height, width, color), dtype=int) # 横向变换，右移
    step = 0
    for j in range(height):
        if step == 0:
            res_img[j] = img[j]
        else:
            res_img[j, :step] = img[j, -step:]
            res_img[j, step:] = img[j, :-step]
        step = (step+a) % width
    img = res_img
    res_img = np.zeros((height, width, color), dtype=int) # 纵向变换，下移
    step = 0
    for i in range(width):
        if step == 0:
            res_img[:, i] = img[:, i]
        else:
            res_img[:step, i] = img[-step:, i]
            res_img[step:, i] = img[:-step, i]
        step = (step+b) % height
    # for i in range(width): #i -> y, j -> x
    #     for j in range(height):
    #         new_i = (i + a*j) % width
    #         new_j = (j + b*new_i) % height
    #         res_img[new_j, new_i] = img[j, i]
    Image.fromarray(np.uint8(res_img)).save('res_a{}_b{}.png'.format(a, b))


arnold("./test.png", 1, 2)