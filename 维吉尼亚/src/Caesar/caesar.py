import string


class Caesar:

    def __init__(self, offset: str) -> None:
        self.offset = offset
        self.lower_str = string.ascii_lowercase
        self.upper_str = string.ascii_uppercase

    def encipher(self, plan_text: str):
        cipher_text = ""
        for chr in plan_text:
            if chr in self.lower_str:
                cipher_text += self.lower_str[(self.lower_str.index(chr) + self.offset) % 26]
            elif chr in self.upper_str:
                cipher_text += self.upper_str[(self.upper_str.index(chr) + self.offset) % 26]
            else:
                cipher_text += chr
        return cipher_text

    def decipher(self, cipher_text: str):
        plan_text = ""
        for chr in cipher_text:
            if chr in self.lower_str:
                plan_text += self.lower_str[(self.lower_str.index(chr) - self.offset) % 26]
            elif chr in self.upper_str:
                plan_text += self.upper_str[(self.upper_str.index(chr) - self.offset) % 26]
            else:
                plan_text += chr
        return plan_text

if __name__ == "__main__":

    ca = Caesar(offset=7)
    print(ca.decipher("mshn{fvb_hyl_zv_zt4ya!}"))
    
