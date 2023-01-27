'''
BYTE1 --
       |--bit0:   Left Control是否按下，按下为1 
       |--bit1:   Left Shift  是否按下，按下为1 
       |--bit2:   Left Alt    是否按下，按下为1 
       |--bit3:   Left GUI    是否按下，按下为1 
       |--bit4:   Right Control是否按下，按下为1  
       |--bit5:   Right Shift 是否按下，按下为1 
       |--bit6:   Right Alt   是否按下，按下为1 
       |--bit7:   Right GUI   是否按下，按下为1 
BYTE2 -- 暂不清楚，有的地方说是保留位
BYTE3--BYTE8 -- 这六个为普通按键
from: https://blog.csdn.net/fjh1997/article/details/105841367
'''
import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-f", type=str, default=None, required=True,
                    help="输入同级目录下的名称")
args  = parser.parse_args()

FILE_PATH = os.path.abspath(args.f)


normalKeys = {
        "04":"a", "05":"b", "06":"c", "07":"d", "08":"e",
        "09":"f", "0a":"g", "0b":"h", "0c":"i", "0d":"j",
        "0e":"k", "0f":"l", "10":"m", "11":"n", "12":"o",
        "13":"p", "14":"q", "15":"r", "16":"s", "17":"t",
        "18":"u", "19":"v", "1a":"w", "1b":"x", "1c":"y",
        "1d":"z","1e":"1", "1f":"2", "20":"3", "21":"4",
        "22":"5", "23":"6","24":"7","25":"8","26":"9",
        "27":"0", "28":"<RET>", "29":"<ESC>", "2a":"<DEL>", "2b":"<ALT>",
        "2c":"<SPACE>","2d":"-","2e":"=","2f":"[","30":"]","31":"\\",
        "32":"<NON>", "33":";","34":"'", "35":"<GA>", "36":",", "37":".",
        "38":"/", "39":"<CAP>", "3a":"<F1>", "3b":"<F2>", "3c":"<F3>", "3d":"<F4>",
        "3e":"<F5>", "3f":"<F6>", "40":"<F7>", "41":"<F8>", "42":"<F9>", "43":"<F10>",
        "44":"<F11>", "45":"<F12>", "4a":"<HOME>", "4c":"<DELETE>", "4d":"<END>", "4f":"<RightArrow>", 
        "50":"<LeftArrow>", "51":"<DownArrow>", "52": "<UpArrow>", "53":"<NumLock>", "54":"/", 
        "55":"*", "56":"-", "57":"+", "58":"<RET>", "59":"1", "5a":"2", "5b":"3", "5c":"4", "5d":"5", 
        "5e":"6", "5f":"7", "60":"8", "61":"9", "62":"0"}
shiftKeys = {
        "04":"A", "05":"B", "06":"C", "07":"D", "08":"E",
        "09":"F", "0a":"G", "0b":"H", "0c":"I", "0d":"J",
        "0e":"K", "0f":"L", "10":"M", "11":"N", "12":"O", 
        "13":"P", "14":"Q", "15":"R", "16":"S", "17":"T",
        "18":"U", "19":"V", "1a":"W", "1b":"X", "1c":"Y",
        "1d":"Z","1e":"!", "1f":"@", "20":"#", "21":"$",
        "22":"%", "23":"^","24":"&","25":"*","26":"(","27":")",
        "28":"<RET>","29":"<ESC>","2a":"<DEL>", "2b":"<ALT>","2c":"<SPACE>",
        "2d":"_","2e":"+","2f":"{","30":"}","31":"|","32":"<NON>","33":"\"",
        "34":":","35":"<GA>","36":"<","37":">","38":"?","39":"<CAP>","3a":"<F1>",
        "3b":"<F2>", "3c":"<F3>","3d":"<F4>","3e":"<F5>","3f":"<F6>","40":"<F7>",
        "41":"<F8>","42":"<F9>","43":"<F10>","44":"<F11>","45":"<F12>", 
        "4a":"<HOME>", "4c":"<DELETE>", "4d":"<END>", "4f":"<RightArrow>", 
        "50":"<LeftArrow>", "51":"<DownArrow>", "52": "<UpArrow>", "53":"<NumLock>", "54":"/", 
        "55":"*", "56":"-", "57":"+", "58":"<RET>", "59":"1", "5a":"2", "5b":"3", "5c":"4", "5d":"5", 
        "5e":"6", "5f":"7", "60":"8", "61":"9", "62":"0"}
with open(FILE_PATH, "r") as f:
    data = f.read().splitlines()

def get_info(original=False):
    output = ""
    for line in data:
        if line[4:6] == "00" :
            continue

        if not original and line[4:6] == "2a":
            output = output[:-1]
            continue

        if line[4:6] in normalKeys:
            if line[4:6] == '2f':
                print(int(line[:2], 16))
            output += shiftKeys[line[4:6]] if (int(line[:2], 16) >> 1 & 1 == 1) or (int(line[:2], 16) >> 5 & 1 == 1) else normalKeys[line[4:6]]
    return output

print(f"原始数据: {get_info(True)}")
flag = get_info().replace('<SPACE>', '').replace('<ALT>', '\t').replace('<CAP>', '').replace('<RET>', '\n')
print(f"正常数据: {flag}")
