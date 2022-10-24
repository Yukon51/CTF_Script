import os
import random
import string
from src import Vigenere

base_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(base_dir)

def demo1():
    # 标准表：CTMZVBDHWFKIXRQGUEJSOPNYAL
    # 密文：TJNZ{LRADVDYJIZ}
    # 密钥：KKPK
    # 明文：FLAG{THISISFLAG}
    col_table = "CTMZVBDHWFKIXRQGUEJSOPNYAL"
    print(Vigenere.Vigenere(key="KKPK", col_table=col_table).decipher("TJNZ{LRADVDYJIZ}"))

def demo2():
    key = "THISISKEY"

    # 生成行单射表打乱的表
    tables = []
    for _ in range(26):
        lis = list(string.ascii_uppercase)
        random.shuffle(lis)
        tables.append(lis)

    cipher_text = Vigenere.Vigenere(key=key, tables=tables).encipher("FLAG{THISISFLAG}")
    # 保存密钥，密文和打乱的表
    with open("题目.txt", "w", encoding="utf-8") as f:
        f.write(f"密钥：{key}\n")
        f.write(f"密文：{cipher_text}\n\n\n")
        f.write("     " + '  '.join(string.ascii_uppercase) + "\n")
        f.write("----------------------------------------------------------------------------------" + "\n")
        for i, lis in enumerate(tables):
            f.write(f"{string.ascii_uppercase[i]} || {'  '.join(lis)}" + "\n")

def demo3():
    key = "THISISKEY"
    tables = "WMLJRYGQOAUEZBFDXCHVNKPTSI,EIMPRXYDOLNHQJBGTAFWCSVZUK,RTSAOKICFHGXMUDYQPZVNJEWBL,WJZCOLHSBPDQMGERTAXNKFUIYV,PGVOSEFZURQNBIMCXTJYWDKALH,BYFVHDPWLJAXMROSGKNIECUZQT,SDYONHIQPJWVLFBXTMGURCEAKZ,KZQYIHOGBLRCPUNXSJTFAEMDWV,ZNIBYWLPRUGXEKQAVFDSCHMJOT,THIOFMLKEQYWUNGZDRCBSPVJXA,GOFSNCTRJZXMAVYWUQPHBIELKD,IYVZSKRMNPTEDBXQOFHJLCAWGU,ELBNRQSOWUADICVMKHFJXPTYZG,NRZTKDYSCEIBJUAHMVQWFGLPOX,OVYMADWSZBERHXJTQPGUINLKCF,ELFWUBOHCDIPRSZQAVTNJKXGMY,AZXVWUSEQJHLIDBOKCRYFNPGTM,AUBMYIRNJFQKXEOWPDTLHCGVZS,UPTZQRCFJHBSIYGDVWXELKAMON,GFATJDCRWOVULSMZPIYHBQXKNE,EARILWTCZGYHKFNXJOUPSDVQMB,YIAMZSDRWKOHLVXEQPCGBJTUFN,CYGHTFEVIONUSLDPXMQWJAZKBR,GTDBHJEZIUOAKCQPLMFSNRXYVW,HUXLZVMNQWJFAOCYBERGKDPTSI,XYODNCZHBAKPTFULIWSQGMJERV"
    tables = [list(i) for i in tables.split(",")]

    vi = Vigenere.Vigenere(key=key, tables=tables)
    print(vi.decipher("DCZC{SFJJQYHXUL}"))

if __name__ == "__main__":
    # demo1()
    demo2() # 加密
    # demo3() # 解密