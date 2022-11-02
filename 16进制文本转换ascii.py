import os
import win32con
import win32clipboard
from rich.table import Table
from rich.console import Console


console = Console()
base_dir = os.path.dirname(os.path.abspath(__file__))

def get_text():
    win32clipboard.OpenClipboard()
    d = win32clipboard.GetClipboardData(win32con.CF_TEXT)
    win32clipboard.CloseClipboard()
    return d.decode('GBK')

def int2str(byte_list, is_add=True):
    ret = []
    if is_add:
        for i in range(256):
            add_text, flag = "", 0
            for number in byte_list:
                num = number+i
                if 31 < num < 127:
                    add_text += chr(num)
                else:
                    add_text += "~"
                    flag = 1
            ret.append([f"+{i}", add_text, flag])
    else:
        for i in range(1, 256):
            add_text, flag = "", 0
            for number in byte_list:
                num = number-i
                if 31 < num < 127:
                    add_text += chr(num)
                else:
                    add_text += "~"
                    flag = 1
            ret.append([f"-{i}", add_text, flag])
    return ret

def show_table(ret, is_all=False):
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("Offset", style="dim", width=6)
    table.add_column("Text")
    for data in ret:
        if data[-1] == 0:
            table.add_row(data[0], f"[bold red]{data[1]}[/]")
        elif is_all:
            table.add_row(data[0], f"{data[1]}")
    console.print(table)

if __name__ == "__main__":
    text = get_text()
    byte_list = [int(text[i:i+2], 16) for i in range(0, len(text), 2)]
    ret = int2str(byte_list, is_add=False)
    ret.extend(int2str(byte_list, is_add=True))

    console.print("Byxs20 Hex Tools:", style="bold blue")
    show_table(ret, is_all=False)
    if console.input("[bold blue]是否需要全部输出? [/]([bold red]y[/]/[bold green]N[/]): ") in ["Y", "y"]:
        show_table(ret, is_all=True)
    os.system("pause")
    # c8e9aca0c3f4e6e5f2a1a0d4e8e5a0e6ece1e7a0e9f3baa0e6ece1e7fbf7e5e6e5efe9e4eae7efe5e4f3e6e9eff2f0e5e6e4e6e7e7e6e4f3e5fd