import os
import argparse
import win32con
import win32clipboard


parser = argparse.ArgumentParser()
parser.add_argument("-f", default=None, required=False, type=str,
                  help="请输入文件路径，没有目录会自动使用剪切板内容")
args = parser.parse_args()

def get_text():
    win32clipboard.OpenClipboard()
    d = win32clipboard.GetClipboardData(win32con.CF_TEXT)
    win32clipboard.CloseClipboard()
    return d.decode('GBK')

ciphey_path = "D:\Python\Scripts\ciphey.exe"
if args.f:
    os.system(f"{ciphey_path} -f {os.path.abspath(args.f)}")
else:
    os.system(f"{ciphey_path} -t {get_text()}")

os.system("pause")
