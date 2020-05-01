import binascii

from Crypto.Util.number import getPrime


def invmod(a, n):
    t, r = 0, n
    new_t, new_r = 1, a
    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r
    if r > 1:
        return 0
    if t < 0:
        t = t + n
    return t


def encryption(m , n, e=3):
    #Чтобы зашифровать текст m: c = m^e(mod n).
    return pow(m,e,n)

def decryption(c,n,d):
    #Чтобы расшифроватьтекст c: m = c^d (mod n).
    return pow(c,d,n)



"""Сгенерируйте 2 случайных простых числа. 
Для теста годятся небольшие числа, так что можно их
 выбрать из таблицы. Назовём их p и
q"""
bitsize = 1024
p = getPrime(int(bitsize/2))
q = getPrime(int(bitsize/2))

'''Пусть n = p * q. Все вычисления в RSA будут по модулю n.'''
n=p*q

'''Пусть t = (p-1)*(q-1) (это функция Эйлера). Эта величина нужна
только для генерации ключа'''
t=(p-1)*(q-1)

'''Пусть e = 3.'''
e=3

'''Вычислите d = invmod(e, t). Например, invmod(17, 3120) = 2753.'''
d=invmod(e,t)
#print(invmod(17,3120))

'''Вашим открытым ключом является [e, n].
 Вашим секретным ключом является [d, n].'''
open_key = [e,n]
secret_key = [d,n]

def test(m=42):
    print(m)
    c=encryption(m,n,e)
    print(c)
    m=decryption(c,n,d)
    print(m)
    '''
    output: >>74088
            >>42
    '''

#test(12546786)

msg=b'this is test'
test(int(binascii.hexlify(msg)))