import string
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-f', type=str, default=None, required=True,
                    help='输入文件名')
args  = parser.parse_args()


with open(args.f, "r") as f:
	data = f.read()


dic = {i: 0 for i in string.ascii_lowercase}

# 词频分析
for i in data:
	if i in dic:
		dic[i] += 1

# 从大到小排序一下
dic = sorted(dic.items(), key=lambda i:i[1], reverse=True)
# [('e', 39915), ('t', 29048), ('a', 26590), ('o', 26141), ('h', 22531), ('n', 21825), ('r', 21650), ('i', 20815), ('s', 19714), ('d', 16617), ('l', 14594), ('u', 9755), ('g', 8619), ('y', 8619), ('w', 8397), ('m', 7394), ('f', 6857), ('c', 6696), ('p', 5548), ('b', 5328), ('k', 4009), ('v', 2908), ('q', 420), ('x', 383), ('j', 370), ('z', 264)]


print(dic, end="\n\n")

# 拿到前16个
ret = "".join(j[0] for index, j in enumerate(dic))
print(ret)