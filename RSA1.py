import random

def primeNumberChecker(num):
    if num > 1:
        for i in range(2, num // 2):
            if (num % i) == 0:
                return False
        return True
    else:
        return False

# Euclid's extended algorithm for finding the multiplicative inverse of two numbers
def gcd(a, b):
    while(b):
        a, b = b, a % b
    return a

def coprime(oe, ophi):
    x = 0
    y = 1
    lx = 1
    ly = 0
    e = oe
    phi = ophi

    while phi != 0:

        t = e // phi
        
        (e, phi) = (phi, e % phi)

        (x, lx) = ((lx - (t * x)), x)
        (y, ly) = ((ly - (t * y)), y)

    if lx < 0:
        lx += ophi
    if ly < 0:
        ly += oe

    return lx

def generate_keypair(p, q):
    n = p * q
    # Phi is the totient of n
    phi = (p - 1) * (q - 1)
    # Choose an integer e such that e and phi(n) are coprime  and 1 < e < phi
    e = random.randrange(1, phi)
    # Use Euclid's Algorithm to verify that e and phi(n) are coprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    # Use Extended Euclid's Algorithm to generate the private key
    d = coprime(e, phi)
    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n)), phi

if __name__ == '__main__':

    isP = False
    isQ = False

    while isP == False:
        p = int(input("Enter a prime number. "))
        if primeNumberChecker(p) == False:
            print("Entered number is not prime. Try again!\n")
        else:
            isP = True

    while isQ == False:
        q = int(input("Enter another prime number not same as above. "))
        if primeNumberChecker(q) == False:
            print("Entered number is not prime. Try again!\n")
        else:
            isQ = True

    if p == q:
        raise ValueError('p and q cannot be equal')
    else:
        (public_key, private_key), totient  = generate_keypair(p, q)
        _, modulus = private_key
        print()
        print("Your public key: ", public_key)
        print("Your private key: ", private_key)
        print()
        print("modulus: ", modulus)
        print()
        f = open("keys.txt", "w")
        f.write(str(private_key[0])+"\n")
        f.write(str(private_key[1])+"\n")
        f.write(str(modulus))
        f.close()
