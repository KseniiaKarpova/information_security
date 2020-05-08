import random
import task_39
from Crypto.Util.number import getPrime
import binascii

bitsize = 1024
p = getPrime(int(bitsize/2))
q = getPrime(int(bitsize/2))
n=p*q
t=(p-1)*(q-1)
e=3
d= task_39.invmod(e,t)
open_key = [e,n]
secret_key = [d,n]
msg=b'this is test'
s=random.randint(1,n-1)
c = task_39.encryption(int(binascii.hexlify(msg)),n)
c1 = (pow(s, e, n) * c) % n
p1 = task_39.decryption(c1,n,d)
print(p1)
p = (task_39.invmod(s,n)*p1) %n
print(p)
print(binascii.unhexlify(bytes(str(p), encoding='utf-8')))

