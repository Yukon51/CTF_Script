'''
Example:
    N = 61366

输出：
    {1: 61366, 2: 30683, 61: 1006, 122: 503, 503: 122, 1006: 61, 30683: 2}

    {X1: Y1, X2: Y2, ..., Xn: Yn}
'''
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', type=int, default=None, required=True,
                    help='输入数字')
args  = parser.parse_args()


N = args.t
ret = {X: int(N / X) for X in range(1, N) if N % X == 0}
print(ret)