file = open("1.mp3", "rb")

# start为第一个private_bit的位置，也就是FF FB XX，XX的这个位置，用010editor看位置，然后填写。
# end为文件最后的位置，也用010editor查看就好了。
start = 0x399D2
end = 0x294C6A

bin_str = ""
while start < end:
    file.seek(start, 0)

    bin_ = bin(ord(file.read(1)))
    
    # 如果padding为0，就为正常情况，如果为1，就是要多1bit。
    if (padding := bin_[-2]) == "1":
        start += 0x1A2
    elif padding == "0":
        start += 0x1A1
    
    # 读取private_bit的bit
    bin_str += bin_[-1]

print(bin_str)
