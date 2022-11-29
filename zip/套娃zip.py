import io
import zipfile
from tqdm import tqdm


zip_src='flag100000_8d0f540c1cc0d892f6d102cfac0982c3.zip' #文件名
with open(zip_src, 'rb') as file:
    buffer = file.read()

pbar = tqdm()
while True:
    if zipfile.is_zipfile(io.BytesIO(buffer)):
        with zipfile.ZipFile(io.BytesIO(buffer), "r") as zf:
            buffer = zf.read(zf.filelist[0].filename)
        pbar.update(1)
    else:
        pbar.close()
        print(buffer)
        break