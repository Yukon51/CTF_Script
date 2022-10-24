import string


class Vigenere:

    def __init__(self, key=None, tables=None, row_table=None, col_table=None) -> None:
        # 正常情况col_table为标准表
        self.key = None if key is None else key.upper()
        self.row_table = string.ascii_uppercase if row_table is None else row_table
        self.col_table = string.ascii_uppercase if col_table is None else col_table
        self.tables = self.create_table() if tables is None else tables

    def create_table(self):
        tables = []
        for offset in range(26):
            lis = [string.ascii_uppercase[(string.ascii_uppercase.index(chr) + offset) % 26] for chr in string.ascii_uppercase]
            tables.append(lis)
        return tables
    
    def encipher(self, plan_text: str):
        """
        先找到明文所在列的位置，再找到密钥所在行的位置，相交的位置就为密文。
        """
        assert self.key is not None, "密钥为空,你不可以进行加密,你只可以进行推出密钥"
        key_offset = 0
        cipher_text = ""
        for chr in plan_text.upper():
            if chr in string.ascii_uppercase:
                col = self.col_table.index(chr)
                col_table = [i[col] for i in self.tables]
                row = self.row_table.index(self.key[key_offset % len(self.key)])
                cipher_text += col_table[row]
                key_offset += 1
            else:
                cipher_text += chr
        return cipher_text

    def decipher(self, cipher_text: str):
        """
        先找到密钥所在行的位置，然后找到密文对应的列的位置，就是明文。
        """
        assert self.key is not None, "密钥为空,你不可以进行加密,你只可以进行推出密钥"
        key_offset = 0
        plan_text = ""
        for chr in cipher_text.upper():
            if chr in string.ascii_uppercase:
                row = self.row_table.index(self.key[key_offset % len(self.key)])
                row_table = self.tables[row]
                col = row_table.index(chr)
                plan_text += self.col_table[col]
                key_offset += 1
            else:
                plan_text += chr
        return plan_text

    def get_key(self, cipher_text, plan_text):
        plan_text = plan_text.upper()
        cipher_text = cipher_text.upper()
        key = ""
        for offset, chr in enumerate(plan_text.upper()):
            if chr in string.ascii_uppercase and cipher_text[offset % len(cipher_text)] in string.ascii_uppercase:
                col = self.col_table.index(chr)
                col_table = [i[col] for i in self.tables]
                row = col_table.index(cipher_text[offset % len(cipher_text)])
                key += self.row_table[row]
        return key

if __name__ == "__main__":
    tables = [
        ["H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G"],
        ["I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H"],
        ["J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I"],
        ["K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
        ["L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"],
        ["M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"],
        ["N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"],
        ["O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"],
        ["P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"],
        ["Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"],
        ["R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q"],
        ["S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R"],
        ["T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S"],
        ["U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"],
        ["V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U"],
        ["W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V"],
        ["X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W"],
        ["Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X"],
        ["Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y"],
        ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"],
        ["B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A"],
        ["C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B"],
        ["D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C"],
        ["E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D"],
        ["F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E"],
        ["G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F"],
    ]

    ve = Vigenere(key="IFYOUARESMARTLIKEIHOPEYOUARE", tables=tables)
    print(ve.decipher("NQXTPBBZXHBYRWHFNASQACLJHVEZ"))
