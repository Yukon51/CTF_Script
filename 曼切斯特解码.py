import re 

 
hex1 = 'AAAAA56A69AA55A95995A569AA95565556' # 0x8893CA58
hex1 = 'AAAAA56A69AA556A965A5999596AA95656'
 
def bintohex(s1):
    s1 = re.findall('.{4}',s1)
    print ('每一个hex分隔:',s1)
    s2 = ''.join(hex(int(i,2)).replace('0x', '') for i in s1)
    print ('ID:', s2.upper())

  
def diffmqst(s):
    s1 = ''
    s = re.findall('.{2}',s)
    cc = '01'
    for i in s:
        s1 += '0' if i == cc else '1'
        cc = i  # 差分加上cc = i

    print ('差分曼切斯特解码:',s1)
    bintohex(s1)

def mqst(s):  #只能算曼切斯特编码,无法算差分
    mdict = {'5': '00', '6': '01', '9': '10', 'A': '11'}
    a1 = ''.join(mdict[i] for i in s)
    print ('曼切斯特解码:   ',a1 )
    bintohex(a1)
    print()

    a2 = ''.join(mdict[i][::-1] for i in s)
    print ('曼切斯特解码2:  ',a2)
    bintohex(a2)


if __name__ == '__main__':
    bin1 = bin(int(hex1, 16))[2:]
    diffmqst(bin1)
    print()
 
    mqst(hex1)