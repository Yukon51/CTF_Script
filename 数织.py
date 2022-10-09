import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', type=str, default=None, required=True,
                    help='输入数织字符串')
args  = parser.parse_args()

template = "MK Version 3.0\n\n"
text = args.t

# 1.获取到col和row
col_text = re.findall("col([0-9/()]*)", text)[0]
row_text = re.findall("row([0-9/()]*)", text)[0]

# 2.分割加过滤''
col_lis = col_text.split("/")
col_lis = list(filter(lambda x: x!="", col_lis))

# 3.分割加过滤''
row_lis = row_text.split("/")
row_lis = list(filter(lambda x: x!="", row_lis))

# 4.构造griddler文件
template += f"{len(col_lis)} {len(row_lis)}\n\n"

#  构造 ? 矩阵
for _ in range(len(col_lis)):
    for _ in row_lis:
        template += " ?"
    template += "\n"
template += "\n"

#  构造每列
for col in col_lis:
    for j in range(len(col)):
        template += f" {col[j]}"
    template += "\n"
template += "\n"

#  构造每行
for row in row_lis:
    for j in range(len(row)):
        template += f" {row[j]}"
    template += "\n"

# 5.保存
with open("out.griddler", "w") as f:
    f.write(template)
