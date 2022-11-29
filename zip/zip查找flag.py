import re, zipfile

z = zipfile.ZipFile('Continue.zip')
for file in z.filelist:
    data = z.read(file).decode()
    if 'NSSCTF{' in data:
        print(re.findall(r'NSSCTF{.+?}', data)[0])
