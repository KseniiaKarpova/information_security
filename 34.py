from Crypto import Random
from Crypto.Cipher import AES
import random
import hashlib

#cipher = AES.new(key, AES.MODE_CBC, iv)
#msg = iv + cipher.encrypt(b'Attack at dawn')

p = 37
g=5
a=random.randint(1, p-1) % p
A = pow(g, a, p)
b=random.randint(1, p-1) % p
B=pow(g, b, p)


def send(from_, to, what):
    print(from_ ," send ", what, " to ", to)


#A->M
#Отправить "p", "g", "A"
send('A', 'M', [p, g, A])
#M->B
#Отправить "p", "g", "p"
send('M', 'B', [p, g, p])
#B->M
#Отправить "B"
send('B', 'M', B)
#M->A
#Отправить "p"
send('M', 'A', p)
sA=pow(p, a, p) #B подменили p
#A->M
#Отправить AES-CBC(SHA1(s)[0:16], iv=random(16), msg) + iv
#msg = b'Stay HOME!'
s_a = hashlib.sha1(str(sA).encode()).digest()[:16]
iv = Random.new().read(AES.block_size)
cipher = AES.new(s_a, AES.MODE_CBC, iv)
msg = iv + cipher.encrypt(b'Attack at dawn!!')
send('A', 'M', msg)
#M->B
#Перенаправить это сообщение B
msg_a = cipher.decrypt(msg)[-16:]
print("decrypt msg = ", msg_a)
send('M', 'B', msg)
#B->M
#Отправить AES-CBC(SHA1(s)[0:16], iv=random(16), A’s msg) + iv
sB=pow(p, b, p)
s_b = hashlib.sha1(str(sB).encode()).digest()[:16]
iv = Random.new().read(AES.block_size)
cipher = AES.new(s_b, AES.MODE_CBC, iv)
msg = iv + cipher.encrypt(msg_a)
send('B', 'M', msg)
#M->A
#Перенаправить это сообщение
send('M', 'A', msg)
