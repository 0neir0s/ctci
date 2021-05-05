import math

def isPrime(n):
    """ is n a prime number ? """
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n%i:
            continue
        return False
    return True

from collections import defaultdict

def crossOff(isPrime, prime, n):
    i = prime*prime
    while i < n:
        isPrime[i] = False
        i += prime

def nextPrime(isPrime, prime, n):
    i = prime + 1
    while i < n:
        if isPrime[i]:
            break
        i += 1
    return i

def sieve(n):
    """ return the dict of all primes till n """
    isPrime = defaultdict(lambda: True)
    isPrime[1] = False
    prime = 2
    while prime <= math.sqrt(n):
        crossOff(isPrime, prime, n)
        prime = nextPrime(isPrime, prime, n)
    return isPrime

print(sieve(100))
