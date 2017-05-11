from math import *

p = 1229 #p, q and d are the private key
q = 1231
n = p*q #n and e are the public key
e = 23 #e and phi(n) should be coprime, check with gcd

def gcd(a, b): #Euclidean algorithm
    if a == 1 or b == 1:
        return 1
    elif a % b == 0:
        return b
    elif a > b:
        return gcd(b, a % b)
    else:
        return gcd(b, a)

#Extended Euclidean algorithm,
def egcd(a, b): # return (g, x, y) a*x + b*y = gcd(x, y)
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

#Multiplicative inverse, finds d = modular multiplicative inverse of e mod phi(n)
def mul_inv(b, m): # x = mul_inv(b) mod m, (x * b) % m == 1
    g, x, _ = egcd(b, m)
    if g == 1:
        return x % m
        
def phi(n): #Euler's totient function
    return (p-1)*(q-1)

def slow_exp(a, b, m): #slow modular exponentiation
    ans = 1
    for _ in range(b):
        ans = (ans*a) % m
    return ans

def mod_exp(a,b): #fast modular exponentiation using squaring
    if b < 0:
        return 1
    elif b == 1:
        return a
    elif b % 2 == 0:
        return mod_exp(a*a, b/2) % n
    else:
        return a * mod_exp(a*a, (b-1)/2) % n
    
'''def mod_exp2(b,e,m):
    if m == 1:
        return 0
    result = 1
    b = b % m
    while e > 0:
        if e % 2 == 1:
            result = (result*b) % m
        e += 1
        b = (b*b) % m
    return result'''

def encrypt(m): 
    c = mod_exp(m,e) #ciphertext
    print(c)
    
def decrypt(c):
    d = mul_inv(e,phi(n)) #finds d
    print("d is {}".format(d))
    print(mod_exp(c,d))
       
    
