import os
import time
import argparse
import zwsp_steg
import webbrowser
from rich.table import Table
from rich.console import Console


parser = argparse.ArgumentParser()
parser.add_argument('-f', type=str, default=None, required=True,
                    help='输入文件名称')
args = parser.parse_args()

console = Console()
base_dir = os.path.dirname(os.path.abspath(__file__))


# 1.read data
with open(args.f, "r", encoding="utf-8") as f:
    data = f.read()

url_dict = [
    ["1", "https://www.mzy0.com/ctftools/zerowidth1/", "src/www.mzy0.com/Unicode.html"],
    ["2", "https://www.mzy0.com/ctftools/zerowidth2/", "src/www.mzy0.com/Offdev.net.html"],
    ["3", "https://330k.github.io/misc_tools/unicode_steganography.html", "src/misc_tools-gh-pages/unicode_steganography.html"],
    ["4", "https://yuanfux.github.io/zero-width-web/", "src/zero-width-web-master/docs/index.html"],
    ["5", "http://www.atoolbox.net/Tool.php?Id=829", "src/一个工具箱/隐藏字符加密.html"]
]

def show_table():
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("WebSite", style="dim", width=8)
    table.add_column("Link")
    for i, info in enumerate(url_dict):
        if i == 0:
            table.add_row(info[0], f"[bold red]{info[1]}[/]")
        else:
            table.add_row(*info[:2])
    console.print(table)

def offline_site(choice):
    url_path = os.path.join(base_dir, url_dict[int(choice)-1][2])
    os.system(url_path)

def open_website(choice, online):
    webbrowser.open(url_dict[int(choice)-1][1], new=0, autoraise=True) if online else offline_site(choice)

def select_website(from_except=False):
    os.system("cls")
    show_table()
    while True:
        if from_except:
            choice = console.input(f"[bold blue][-] 无法正常解开, 请选择您想要的使用的网站? (1~{len(url_dict)+1}, 回车则使用默认网站): [/]")
        else:
            choice = console.input(f"[bold blue][-] 选择您想要的使用的网站? (1~{len(url_dict)+1}, 回车则使用默认网站): [/]")

        if choice == "":
            choice = "1"
            break
        elif choice in [str(i) for i in range(1, len(url_dict) + 1)]:
            break
        else:
            console.print("[-] 输入错误, 请重新输入!", style="bold blue")

    online = console.input("[bold blue][-] 是否在线访问网站? [/]([bold green]y[/]/[bold red]N[/]): ") in ["y", "Y"]
    open_website(choice, online)

if __name__ == "__main__":
    try:
        console.print("[-] 已经为您解开, 结果如下: ", style="bold blue")
        console.print(zwsp_steg.decode(data), style="bold red")
        if console.input("[bold blue][-] 是否需要网站呢? [/]([bold green]y[/]/[bold red]N[/]): ") in ["y", "Y"]:
            select_website()
        else:
            console.print("[-] 欢迎下次使用!", style="bold blue")
            time.sleep(0.5)
    except TypeError:
        select_website(from_except=True)
        
        