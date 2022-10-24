import os
import string
from rich.console import Console
from src import Vigenere, Caesar


console = Console()

def is_Conform(text):
    # 输入内容在a-z或者A-Z之间
    if text == "":
        return False
    return all(chra in string.ascii_letters or ord(chra) in string.ascii_uppercase for chra in text)

def input_key():
    key = console.input("[bold red][+] Input Key: [/bold red]")
    if is_Conform(key):
        return key
    console.print("[-] 密钥格式有误!", style="bold red")
    exit(-1)

def input_table():
    table = console.input("[bold red][+] 请输入标注表(回车则默认使用标准表): [/bold red]")

    if table == "": # 如果标准表为空返回None
        return None
    if len(table) == 26 and is_Conform(table): # 判断标准表是否为26位，是否满足输入内容在a-z或者A-Z之间
        return table.upper()
    console.print("[-] 标准表格式有误!", style="bold red")
    exit(-1)

def input_tables():
    tables = console.input("[bold red][+] 请输入26x26密码表(回车则默认使用标注密码表): [/bold red]")
    if tables == "":
        return None
    tables = [list(i) for i in tables.split(",")]
    return tables

def caesar(plan_text):
    # 使用凯撒遍历常规偏移的情况
    console.print("[-] 常规偏移:", style="bold magenta")
    for offset in range(1, 26):
        console.print("[-] [bold magenta]offset[/bold magenta]: [bold blue]%2s[/bold blue], [bold magenta]Cipher Text[/bold magenta]: %s" % (offset, Caesar.Caesar(offset=offset).decipher(plan_text)), style="bold red on white")

def output_table(tables, plan_text=None, cipher_text=None, encipher=False):
    if encipher:
        console.print(f"\n[-] 修改行标准表 Cipher Text: {Vigenere.Vigenere(key, tables=tables, col_table=table).encipher(plan_text)}", style="bold red on white")
        console.print(f"[-] 修改列标准表 Cipher Text: {Vigenere.Vigenere(key, tables=tables, row_table=table).encipher(plan_text)}", style="bold red on white")
        console.print(f"[-] 修改列和列标准表 Cipher Text: {Vigenere.Vigenere(key, tables=tables, col_table=table, row_table=table).encipher(plan_text)}", style="bold red on white")
    else:
        console.print(f"\n[-] 修改行标准表 Plan Text: {Vigenere.Vigenere(key, tables=tables, col_table=table).decipher(cipher_text)}", style="bold red on white")
        console.print(f"[-] 修改列标准表 Plan Text: {Vigenere.Vigenere(key, tables=tables, row_table=table).decipher(cipher_text)}", style="bold red on white")
        console.print(f"[-] 修改列和列标准表 Plan Text: {Vigenere.Vigenere(key, tables=tables, col_table=table, row_table=table).decipher(cipher_text)}", style="bold red on white")

if __name__ == "__main__":
    console.print("Byxs20's Vigenere Cipher Tools", style="bold magenta")

    if console.input("[bold magenta][+] 请问是否需要加密?(回车默认为解密)[/bold magenta]([bold red]y[/bold red]/[bold blue]N[/bold blue]): ") in ["N", ""]:
        cipher_text = console.input("[bold red][+] Input Cipher Text: [/bold red]")
        key = input_key()
        table = input_table()
        tables = input_tables()

        if cipher_text == "":
            console.print("[-] 密文格式有误!", style="bold red")
            exit(-1)
        
        if table is None:
            plan_text = Vigenere.Vigenere(key, tables=tables).decipher(cipher_text)
            console.print(f"\n[-] Plan Text: {plan_text}", style="bold red")
            caesar(plan_text)
        else:
            output_table(tables=tables, cipher_text=cipher_text, encipher=False)
    else:
        plan_text = console.input("[bold red][+] Input Plan Text: [/bold red]")
        key = input_key()
        table = input_table()
        tables = input_tables()

        if plan_text == "":
            console.print("[-] 明文格式有误!", style="bold red")
            exit(-1)

        if table is None:
            plan_text = Vigenere.Vigenere(key, tables=tables).encipher(plan_text)
            console.print(f"\n[-] Cipher Text: {plan_text}", style="bold red")
            caesar(plan_text)
        else:
            output_table(tables=tables, plan_text=plan_text, encipher=True)