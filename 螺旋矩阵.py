import os
import gmpy2
import argparse

# from https://blog.csdn.net/GW_wg/article/details/120406192
parser = argparse.ArgumentParser()
parser.add_argument('-f', type=str, default=None, required=True,
                    help='输入文件名称')
args = parser.parse_args()

file_path = os.path.abspath(args.f)
file_name, file_suffix = os.path.splitext(file_path)[0].split("\\")[-1], os.path.splitext(file_path)[1]

def function(n):
    matrix = [[0] * n for _ in range(n)]

    number = 1
    left, right, up, down = 0, n - 1, 0, n - 1
    while left < right and up < down:
        # 从左到右
        for i in range(left, right):
            matrix[up][i] = number
            number += 1

        # 从上到下
        for i in range(up, down):
            matrix[i][right] = number
            number += 1

        # 从右向左
        for i in range(right, left, -1):
            matrix[down][i] = number
            number += 1

        for i in range(down, up, -1):
            matrix[i][left] = number
            number += 1
        left += 1
        right -= 1
        up += 1
        down -= 1
    # n 为奇数的时候，正方形中间会有个单独的空格需要单独填充
    if n % 2 != 0:
        matrix[n // 2][n // 2] = number
    return matrix

if __name__ == '__main__':
    with open(file_path,'rb') as f:
        data = f.read()
    
    sqrt_num = gmpy2.iroot(len(data), 2)[0]
    lis = function(sqrt_num)
    lis = sum(lis, [])

    with open(f"spiral_{file_name}{file_suffix}", "wb") as f:
        for i in lis:
            f.write(data[i-1].to_bytes(1, byteorder="big", signed=False))
