from Crypto import Random
from Crypto.Cipher import AES
import random
import hashlib
#----------------------
ACK = "I got a message"

p = 37
g = 5

def send(from_, to, what):
    print(from_ ," send ", what, " to ", to)

#----------------------

def attack(falseG):
    # A->B
    # Отправить "p", "g"
    send('A', 'M', [p,g])
    send('M','B',[p, falseG])
    # B->A
    # Отправить ACK
    send('B','M',ACK)
    send('M','A', ACK)
    # A->B
    # Отправить "A"
    a = random.randint(1, p - 1) % p# secret key
    A = pow(g, a, p) #public key
    send('A', 'M', A)
    send('M', 'B', A)
    # B->A
    # Отправить "B"
    b = random.randint(1, p - 1) % p
    B = pow(falseG, b, p)
    send('B', 'M', B)
    send('M', 'A', B)
    # A->B
    # Отправить AES-CBC(SHA1(s)[0:16], iv=random(16), msg) + iv
    sA = pow(B, a, p) # shared key
    s_a = hashlib.sha1(str(sA).encode()).digest()[:16]
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(s_a, AES.MODE_CBC, iv)
    msg = iv + cipher.encrypt(b'Attack at dawn!!')
    send('A', 'M', msg)
    msg_a = cipher.decrypt(msg)[-16:]
    print("decrypt msg (M know this) = ", msg_a)
    send('M', 'B', msg)

    # B->A
    # Отправить AES-CBC(SHA1(s)[0:16], iv=random(16), сообщение от A) + iv
    sB = pow(A, b, p)

    s_b = hashlib.sha1(str(sB).encode()).digest()[:16]
    print('key= ', sA)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(s_b, AES.MODE_CBC, iv)
    msg = iv + cipher.encrypt(msg_a)
    send('B', 'M', msg)
    send('M', 'A', msg)
    msg_b = cipher.decrypt(msg)[-16:]
    print("decrypt msg (B know this) = ", msg_b)

print('-------------- g = 1 ----------------')
attack(1)

print('-------------- g = p ----------------')
attack(p)


print('-------------- g = p-1 ----------------')
attack(p-1)