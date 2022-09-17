import os
import zlib
import struct
import argparse
import itertools


parser = argparse.ArgumentParser()
parser.add_argument("-f", type=str, default=None, required=True,
                    help="输入同级目录下图片的名称")
args  = parser.parse_args()

png_name = args.f.split("\\")[-1]
base_dir = os.getcwd()
png_dir = os.path.join(base_dir, png_name)

bin_data = open(png_dir, 'rb').read()
crc32key = zlib.crc32(bin_data[12:29]) # 计算crc
original_crc32 = int(bin_data[29:33].hex(), 16) # 原始crc


if crc32key != original_crc32: # 计算crc对比原始crc
    for width, height in itertools.product(range(4095), range(4095)): # 理论上0x FF FF FF FF，但考虑到屏幕实际/cpu，0x 0F FF就差不多了，也就是4095宽度和高度
        data = bin_data[12:16] + struct.pack('>i', width) + struct.pack('>i', height) + bin_data[24:29]
        crc32 = zlib.crc32(data)
        if(crc32 == original_crc32): # 计算当图片大小为width:height时的CRC校验值，与图片中的CRC比较，当相同，则图片大小已经确定
            with open(os.path.join(base_dir, f"fix_{png_name}"), "wb") as f:
                print(f"CRC32: {hex(original_crc32)}")
                print(f"宽度: {width}, hex: {hex(width)}")
                print(f"高度: {height}, hex: {hex(height)}")
                f.write(bin_data[:16] + struct.pack(">i", width) + struct.pack(">i", height) + bin_data[24:])