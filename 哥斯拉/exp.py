import gzip
import base64

def encode(D, K):
	D = list(D)
	for i in range(len(D)):
		c = K[i + 1 & 15]
		D[i] = D[i] ^ c
	return bytes(D)

key = b"d8ea7326e6ec5916"
cipher_text = "J+5pNzMyNmU2mij7dMD/qHMAa1dTUh6rZrUuY2l7eDVot058H+AZShmyrB3w/OdLFa2oeH/jYdeYr09l6fxhLPMsLeAwg8MkGmC+Nbz1+kYvogF0EFH1p/KFEzIcNBVfDaa946G+ynGJob9hH1+WlZFwyP79y4/cvxxKNVw8xP1OZWE3"

out = encode(base64.b64decode(cipher_text), key)
print(gzip.decompress(out))