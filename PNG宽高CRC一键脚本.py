import zlib
import struct
import binascii
import argparse
import itertools


parser = argparse.ArgumentParser()
parser.add_argument("-f", type=str, default=None, required=True,
                    help="输入同级目录下图片的名称")
args  = parser.parse_args()


image_data = open(args.f, 'rb')
bin_data = image_data.read()
crc32key = zlib.crc32(bin_data[12:29])  # 使用函数计算
if crc32key == int(bin_data[29:33].hex(), 16):  # 对比算出的CRC和原本的CRC
    print('宽高没有问题')
else:
    print('宽高被改了')

    input_ = input("是否CRC爆破宽高? (Y/n):")
    if input_ not in ["Y", "y", ""]:
        exit()
    else:
        crcbp = open(args.f, "rb").read()    #打开图片
        crc32frombp = int(crcbp[29:33].hex(), 16)     #读取图片中的CRC校验值
        for i, j in itertools.product(range(4000), range(4000)):
            data = crcbp[12:16] + \
                struct.pack('>i', i)+struct.pack('>i', j)+crcbp[24:29]
            crc32 = binascii.crc32(data) & 0xffffffff
            if(crc32 == crc32frombp):            #计算当图片大小为i:j时的CRC校验值，与图片中的CRC比较，当相同，则图片大小已经确定
                print(i, j)
                print('hex:', hex(i), hex(j))
                exit(0)