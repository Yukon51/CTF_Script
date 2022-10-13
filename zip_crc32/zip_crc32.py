import os
import re
import copy
import zipfile
import argparse
import itertools
import subprocess
from tqdm import tqdm
from rich.console import Console
from prettytable import PrettyTable


parser = argparse.ArgumentParser()
parser.add_argument("-f", type=str, default=None, required=True,
                    help="输入同级目录下文件的名称")
args  = parser.parse_args()

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.abspath(args.f)
save_dir = os.path.dirname(file_path)

console = Console()
z = zipfile.ZipFile(file_path)
PATTERNS = ["4 bytes: (.*?) {", "5 bytes: (.*?) \(", "6 bytes: (.*?) \("]


zip_info = []
name_list = z.namelist()
for file_name in name_list:
    if file_name.endswith(".txt"):
        info = z.getinfo(file_name)
        hex_crc = hex(info.CRC)
        size = info.file_size
        zip_info.append([file_name, size, hex_crc])

for i, (file_name, size, hex_crc) in enumerate(zip_info):
    res = subprocess.Popen(f"python {base_dir}/crc32-master/crc32.py reverse {hex_crc}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result = res.stdout.read().decode('gbk').replace("\r\r\n", "\r\n")

    pwds = []
    if size == 4:
        pwds = re.findall(PATTERNS[0], result)
    elif size == 5:
        pwds = re.findall(PATTERNS[1], result)
    elif size == 6:
        pwds = re.findall(PATTERNS[2], result)

    zip_info[i].append(pwds)


tables = copy.deepcopy(zip_info)
for i, info in enumerate(zip_info):
    pwds = info[-1]

    if len(pwds) > 1:
        tables[i][-1] = "\033[31m%s\033[0m" % (pwds[0])
        tables[i].append("\033[31m%s\033[0m" % "True")
    elif len(pwds) == 1:
        tables[i][-1] = pwds[0]
        tables[i].append("False")
    else:
        tables[i][-1] = "\033[31m%s\033[0m" % "None"
        tables[i].append("\033[31m%s\033[0m" % "*")

table = PrettyTable()
table.title = "Byxs20's Zip Crc32 Tools"
table.field_names = ["File name", "Size", "Checksum", "Text", "More"]
table.add_rows(tables)
print(table)


if all(info[-1] == "False" for info in tables):
    console.print("按顺序拼接在一起: [bold magenta]" + "".join(info[-2] for info in tables) + "[/bold magenta]")


# 待修复: 如果zip文件里面有出现没有被crc32爆破出来的就无法生成字典
if console.input("是否需要生成字典: ([bold red]y[/bold red]/[bold green]N[/bold green]): ") in ["Y", "y"]:
    with open(os.path.join(save_dir, "output.dic"), "w") as f:
        with tqdm(itertools.product(*[info[-1] for info in zip_info]), desc="Generate Dictionary: ") as bar:
            for i in bar:
                f.write("".join(i) + "\n")
    print("Generate Dictionary Finish!")


if console.input("是否需要导出csv: ([bold red]y[/bold red]/[bold green]N[/bold green]): ") in ["Y", "y"]:
    with open(os.path.join(save_dir, "output.csv"), "w") as f:
        f.write(", ".join(["File name", "Size", "Checksum", "Text"]) + "\n")
        for info in zip_info:
            for i in info:
                if not isinstance(i, list):
                    f.write(f"{str(i)}, ")
                else:
                    f.write('   '.join(i))
            f.write("\n")
