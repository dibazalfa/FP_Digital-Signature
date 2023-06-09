import random
import os
import sys

def rabinMiller(num):
   s = num - 1
   t = 0
   
   while s % 2 == 0:
      s = s // 2
      t += 1
   for trials in range(5):
      a = random.randrange(2, num - 1)
      v = pow(a, s, num)
      if v != 1:
         i = 0
         while v != (num - 1):
            if i == t - 1:
               return False
            else:
               i = i + 1
               v = (v ** 2) % num
      return True
   
def isPrime(num):
   if (num < 2):
      return False
   lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 
   67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 
   157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 
   251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313,317, 331, 337, 347, 349, 
   353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 
   457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 
   571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 
   673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 
   797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 
   911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
	
   if num in lowPrimes:
      return True
   for prime in lowPrimes:
      if (num % prime == 0):
         return False
   return rabinMiller(num)

def generateLargePrime(keysize = 1024):
   while True:
      num = random.randrange(2**(keysize-1), 2**(keysize))
      if isPrime(num):
         return num
    
def generateKeys(keysize=1024):
    e = d = N = 0

    p = generateLargePrime(keysize)
    q = generateLargePrime(keysize)

    # print("p :", p)
    # print("q :", q)

    N = p*q
    phiN = (p - 1) * (q - 1)

    while True:
        e = random.randrange(2 ** (keysize - 1), 2 ** keysize - 1)
        if (isCoPrime(e,phiN)):
            break

    d = modilarInv(e,phiN)

    return e, d, N

def generateLargePrime(keysize):
    """
        return bilangan prima dengan jumlah bit sebesar keysize
    """
    
    while True:
        num = random.randrange(2 ** (keysize - 1), 2 ** keysize - 1)
        if (isPrime(num)):
            return num

def isCoPrime(p, q):
    """
        return true kalau gcd(p,q) = 1
        relatif prima
    """
    return gcd(p, q) == 1

def gcd(p, q):
    """
        euclidean algoritm → mencari fpb p dan q
    """
    while q:
        p, q = q, p % q
    return p

def egcd(a,b):
    s = 0; old_s = 1
    t = 1; old_t = 0
    r = b; old_r = a

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    
    #return gcd, x, y
    return old_r, old_s, old_t


def modilarInv(a,b):
    gcd, x ,y = egcd(a,b)

    if x <0:
        x += b

    return x

def enkripsi(e, N, text):
    cipher = ""

    for c in text:
        m = ord(c)
        cipher += str(pow(m, e, N)) + " "

    return cipher

def dekripsi(d, N, cipher):
    text = ""

    parts = cipher.split()
    for part in parts:
        if part:
            c = int(part)
            text += chr(pow(c, d, N))

    return text

def dekripsihex(e, N, text):
    cipher = ""
    m = ""
    
    for c in text:
        m += str(ord(c))
        
        cipher = hex(pow(int(m), e, N)).replace("0x","")+" "
    # print (hex(int(m)))
    return cipher

def enkripsihex(d, N, cipher):
    text = ""
    parts = cipher.split()
    for part in parts:
        if part:
            c = int(part,16)
            text += hex(pow(c, d, N))
    # print (f"c : {c}")
    return text

def writeKey(filename):
    keySize = 1024
    e, d, N = generateKeys(keySize) 
    if os.path.exists('%s.pub' % (filename)) or os.path.exists('%s.pri' % (filename)):
        sys.exit('WARNING: The file %s.pub or %s,.pri already exists! Use a different name or delete these files and re-run this program.' % (filename, filename))

    fo = open('%s.pub' % (filename), 'w')
    fo.write('%s,%s,%s' % (keySize, N, e))
    fo.close()

    fo = open('%s.pri' % (filename), 'w')
    fo.write('%s,%s,%s' % (keySize, N, d))
    fo.close()
    

# def maintest():
#     print("RSA")

#     keysize = int(input("Masukkan keysize : "))

#     e, d, N = generateKeys(keysize) 

#     text = "absjv12345"

#     enc = dekripsihex(e, N, text)
#     print(f"Text :{text}")
#     print(f"e :{e}")
#     print(f"d :{d}")
#     print(f"N :{N}")
#     print(f"enc :{enc}")
#     dec = enkripsihex(d, N, enc)

#     print(f"dec :{dec}")

# maintest()

