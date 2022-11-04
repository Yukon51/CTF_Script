import os
import re
import pyshark
import argparse
from collections import Counter
from rich.console import Console


parser = argparse.ArgumentParser()
parser.add_argument('-f', type=str, default=None, required=True,
                    help='输入文件名称')
args = parser.parse_args()


console = Console()

while True:
    if (dis_filter := console.input("[bold blue][+] 请输入WireShark的过滤器: [/]")) != "":
        break
    else:
        console.print("[-] 输入有误, 请重新输入!")

while True:
    if (re_pattern := console.input("[bold blue][+] 请输入正则表达式: [/]")) != "":
        break
    else:
        console.print("[-] 输入有误, 请重新输入!")

while True:
    length = console.input("[bold blue][+] 请输入FLAG长度: [/]")
    try:
        length = int(length)
        break
    except ValueError:
        console.print("[-] 输入有误, 请输入正整数!", style="bold red")

cap = pyshark.FileCapture(args.f, display_filter=dis_filter)
cap.set_debug()

flag = list(length * "~")
for c in cap:
    ret = re.findall(re_pattern, c.http.request_full_uri)
    if ret != []:
        try:
            index, char = ret[0]
            index = int(index)
            flag[index-1] = chr(int(char))
        except ValueError:
            console.print(f"[bold red][-] 正则表达式匹配错误: [/]{ret}", style="bold bold")
            os.system("pause")
            exit(-1)

if Counter(flag).most_common()[0][0] == "~":
    console.print(f"[bold blue][-] flag中出现最多的为~, 出现了{Counter(flag).most_common()[0][1]}次, 可能是正则表达式错误了: [/]{''.join(flag)}" , style="bold red")
else:
    console.print(f"[bold blue][-] 输出: [/]{''.join(flag)}" , style="bold red")
    os.system("pause")