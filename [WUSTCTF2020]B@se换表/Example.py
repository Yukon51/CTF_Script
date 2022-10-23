import base64
import itertools


cipher_text = "MyLkTaP3FaA7KOWjTmKkVjWjVzKjdeNvTnAjoH9iZOIvTeHbvD=="

base64_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
table = "JASGBWcQPRXEFLbCDIlmnHUVKTYZdMovwipatNOefghq56rs****kxyz012789+/"

# # 找到缺失的****
# for i in base64_table:
#     if i not in character:
#         print(i, end="")

loss = ["j", "u", "3", "4"]

for i in (itertools.permutations(loss, 4)):
    tableNew = table.replace("****", "".join(i))
    # 1.换表
    maketrans = str.maketrans(tableNew, base64_table)
    # 2.使用新表转换字符串
    translate = cipher_text.translate(maketrans)
    # 3.Base64解码
    flag = base64.b64decode(translate)
    print(flag)