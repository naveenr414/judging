import math 

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, (y - (b // a) * x), x)


def gcd(a,b):
    if(b==0):
        return a
    return gcd(b,a%b)

def lcm(a,b):
    return int(a*b/gcd(a,b))

def multiplicativeInverse(a,b):
    return egcd(a,b)[1]%b

def decryptMessage(p,q,e,c):
    totient = (p-1)*(q-1)

    d = multiplicativeInverse(e,totient)

    return pow(c,d,p*q)

def pollardRho(n, seed=2, f=lambda x: x**2 + 1):
   x, y, d = seed, seed, 1
   while d == 1:
     x = f(x) % n
     y = f(f(y)) % n
     d = gcd((x - y) % n, n)
   return None if d == n else d

def find_invpow(x,n):
    """Finds the integer component of the n'th root of x,
    an integer such that y ** n <= x < (y + 1) ** n.
    """
    high = 1
    while high ** n <= x:
        high *= 2
    
    low = high//2
    while low < high:
        mid = (low + high) // 2
        if low < mid and mid**n < x:
            low = mid
        elif high > mid and mid**n > x:
            high = mid
        else:
            return mid
    return mid + 1

def smallExponent(e,nArray,cArray):
    k = 0
    for i in range(0,len(nArray)):
        c_i = cArray[i]
        allOthers = 1
        for j in range(0,len(nArray)):
            if j!= i:
                allOthers*=nArray[j]
        r=c_i*(allOthers)*multiplicativeInverse(allOthers,nArray[i])
        k+=r

    allProduct = 1
    for i in range(0,len(nArray)):
        allProduct*=nArray[i]
    
    return find_invpow(k%allProduct,e)

#Continued Fractions 
def cf_expansion(n, d):
    e = []

    q = n // d
    r = n % d
    e.append(q)

    while r != 0:
        n, d = d, r
        q = n // d
        r = n % d
        e.append(q)

    return e

#See what continued fractions become
def convergents(e):
    n = [] # Nominators
    d = [] # Denominators

    for i in range(len(e)):
        if i == 0:
            ni = e[i]
            di = 1
        elif i == 1:
            ni = e[i]*e[i-1] + 1
            di = e[i]
        else: # i > 1 
            ni = e[i]*n[i-1] + n[i-2]
            di = e[i]*d[i-1] + d[i-2]

        n.append(ni)
        d.append(di)
    return (n,d)

def wiener(e,n,c):
    frac = cf_expansion(e,n)
    converges = convergents(frac)


    minDistance = 10000000000
    minP = 0
    minQ = 0
    
    for q in range(0,len(converges[0])):
        i = converges[0][q]
        j = converges[1][q]


        if(i==0):
            continue
        phi = (e*j-1)//i

        b = (phi-n-1)
        discriminant = b**2-4*n

        
        if(discriminant>=0):
            root = find_invpow(discriminant,2)
            pp = ((-1*b)+root)//2
            pq = ((-1*b)-root)//2
            distance = abs(pp*pq-n)
            if(distance<minDistance):
                minDistance = distance
                minP = pp
                minQ = pq

    if(minDistance<2):
        return decryptMessage(minQ,minP,e,c)

    else:
        return minDistance     

from Crypto.PublicKey import RSA
key = RSA.importKey(open('rsa.pub').read())
n = key.n
print(n)
