import sys

import task_39
from Crypto.Util.number import getPrime
import binascii
import math

def floorRoot(n, s):


    b =len(bin(n)[2:])
    p = math.ceil(b / s)
    x = 2 ** p
    while x > 1:
        y = (((s - 1) * x) + (n // (x ** (s - 1)))) // s
        if y >= x:
            return x
        x = y
    return 1


msg=b'this is test'
bitsize = 1024
e=3


p0 = getPrime(int(bitsize/2))
q0 = getPrime(int(bitsize/2))
n0=p0*q0
t0=(p0-1)*(q0-1)
d0=task_39.invmod(e,t0)
open_key0 = [e,n0]
secret_key0 = [d0,n0]

p1 = getPrime(int(bitsize/2))
q1 = getPrime(int(bitsize/2))
n1=p1*q1
t1=(p1-1)*(q1-1)
d1=task_39.invmod(e,t1)
open_key1 = [e,n1]
secret_key1 = [d1,n1]

p2 = getPrime(int(bitsize/2))
q2 = getPrime(int(bitsize/2))
n2=p2*q2
t2=(p2-1)*(q2-1)
d2=task_39.invmod(e,t2)
open_key2 = [e,n2]
secret_key2 = [d2,n2]

#print(binascii.hexlify(msg))

c0 = task_39.encryption(int(binascii.hexlify(msg)),n0)
c1 = task_39.encryption(int(binascii.hexlify(msg)),n1)
c2 = task_39.encryption(int(binascii.hexlify(msg)),n2)

print(0,'c,n = ', c0, n0)
print(1,'c,n = ', c1, n1)
print(2,'c,n = ', c2, n2)

m_s_0 =n1*n2
m_s_1 =n0*n2
m_s_2 =n0*n1

result = ((c0*m_s_0 * task_39.invmod(m_s_0,n0)) +
(c1*m_s_1 * task_39.invmod(m_s_1,n1))+
(c2*m_s_2 * task_39.invmod(m_s_2,n2))) % (n0*n1*n2)

str = str(floorRoot(result,3))
print(binascii.unhexlify(bytes(str, encoding='utf-8')))


