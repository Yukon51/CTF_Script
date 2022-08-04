import string
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-f', type=str, default=None, required=True,
                    help='输入文件名称')
args  = parser.parse_args()

# ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/
key = string.ascii_uppercase + string.ascii_lowercase + string.digits + "+/"

# 1.获取密文
# 1.1 读取文件
with open(args.f, "r") as f:
    data = f.readlines()
data = [i.replace("\n", "") for i in data]

# 1.2 把cipher填到这个地方
# cipher = '''
# '''
# data = cipher.splitlines()

# base64隐写解码
'''
1.依次读取每行，从中提取出隐写位。
2.如果最后没有‘=’，说明没有隐写位，跳过。
3.如果最后是一个‘=’，说明有两位隐写位，将倒数第二个字符转化为对应的二进制索引，然后取后两位。
4.如果最后是两个‘=’，说明有四位隐写位，将倒数第三个字符转化为对应的二进制索引，然后取后四位。
5.将每行提取出的隐写位依次连接起来，每8位为一组转换为ASCII字符，最后不足8位的丢弃。
'''
binstring = ""
for cipher in data:
    flag = 0
    if cipher[-1:] == "=":
        flag = 1
        if cipher[-2:] == "==":
            flag = 2
    
    if flag == 1:
        binstring += bin(key.index(cipher[-2])).zfill(8)[-2:]
    elif flag == 2:
        binstring += bin(key.index(cipher[-3])).zfill(8)[-4:]

print(binstring)
print(len(binstring))
print(len(binstring) / 8)
