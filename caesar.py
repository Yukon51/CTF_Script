import string
import argparse

# 在线网站: https://planetcalc.com/1434/

parser = argparse.ArgumentParser()
parser.add_argument("-t", type=str, default=None, required=True,
                    help="输入凯撒加密的字符串")
args  = parser.parse_args()


asc = string.ascii_letters

# 一共是25种情况，26的时候和密文一样
for i in range(1, 26):
    dic = {c: asc[(asc.index(c) + i) % 26] for c in asc}
    m = "".join(dic.get(j, j) for j in args.t)
    print(i, m)

'''
gmbh| xxxxxxxxx ~
gmbh转换为ascii,然后-1,再转为ascii,等于flag{ xxxxxx }
'''
if "gmbh" in args.t[:5]:
    input_ = input("可能是先转换ascii - 1,再转换ascii. 是否尝试? (Y/n):")
    if input_ not in ["Y", "y", ""]:
        exit()
    else:
        print("".join(chr(ord(i) - 1) for i in args.t))