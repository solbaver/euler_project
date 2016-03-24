#this decision is the third problem of the project Euler
import math

n = 600851475143

#search for prime numbers 

def primes(n):
    primes = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            primes.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        primes.append(n)
    return primes

print max(primes(n))
