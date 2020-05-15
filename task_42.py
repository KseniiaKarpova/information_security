from binascii import hexlify, unhexlify
from hashlib import sha1
import task_39
import task_40
from Crypto.Util.number import getPrime


def verify_signature(m, sig, e, n):
    hexsig = hex(pow(sig, e, n))[2:-1]
    index = hexsig.index('ff00')
    hex = hexsig[index + 4:index + 44]
    return sha1(m).hexdigest() == hex


bitsize = 1024
p = getPrime(int(bitsize/2))
q = getPrime(int(bitsize/2))
n=p*q
t=(p-1)*(q-1)
e=3
d=task_39.invmod(e,t)
open_key = [e,n]
secret_key = [d,n]
mes = "hi mom".encode()
h = sha1(mes).digest()
mystr = b'\x00\x01\xff\x00'
mystr += h
mystr += (int(bitsize / 8) - len(mystr)) * b'\x00'
forged = task_40.floorRoot(int.from_bytes(mystr, "big"), e)+1
#print(forged.to_bytes((forged.bit_length() + 7) // 8, "big"))
verified = verify_signature(mes, forged, e, n)
print("Valid signature?",verified)
print('m = ',mes,  forged)


