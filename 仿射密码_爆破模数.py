import string


letters = string.ascii_letters

def ext_euclid(a, m):
    if m == 0:
        return 1, 0
    else:
        x, y = ext_euclid(m, a % m)
        x, y = y, (x - (a // m) * y)
        return x,y

def decode(encodes, a, b, n):
    decode_str = ''
    x = ext_euclid(a,n)
    a = x[0]
    if a < 0:
        a = a + n
    for s in encodes:
        if s in letters:
            z = letters.find(s) % n
            y = a * (z - b) % n
            if s.isupper():
                y += n
            decode_str += letters[y]
        else:
            decode_str += s
    return decode_str

if __name__ == '__main__':
    s = 'oelb{6d332l0-22ck-2b1n-a35i-125f3qe125l1}'
    a = 146442
    b = 428428

    for i in range(1,26):
        d = decode(s, a, b, i)
        print ("模数：",i , d)
