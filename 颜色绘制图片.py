import itertools
from PIL import Image

img = Image.open("./misc57.png")
new_img = Image.new("RGB", (img.width, img.height), color=(255, 255, 255))
black_img = Image.new("RGB", (1, 1), color=(0, 0, 0))

colors = []
for y, x in itertools.product(range(img.height), range(img.width)):
    color = img.getpixel((x, y))
    if color in colors:
        new_img.paste(black_img, (x, y))

new_img.show()

