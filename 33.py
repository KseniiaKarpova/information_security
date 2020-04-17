import random
import hashlib
'''
p=37
g=5
a=random.randint(1,100) % p
A=(g**a) % p

b=random.randint(1,100) % p
B=(g**b) % p

s=(B**a) % p

print(s)

s=(A**b) % p
print(s)

key =hashlib.sha256(bytes(s))
hex_dig = key.hexdigest()
print(hex_dig)
'''

p = 0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361bb9ed529077096966d670c354e4abc9804f1746c08ca237327fffffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024

g=2
a=random.randint(1,100) % p
A=(g**a) % p

b=random.randint(1,100) % p
B=(g**b) % p

s=(B**a) % p

print(s)

s=(A**b) % p
print(s)

key =hashlib.sha256(bytes(s))
hex_dig = key.hexdigest()
print(hex_dig)