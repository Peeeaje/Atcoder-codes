import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=" ")


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=" ")


N = from_readline()[0]


def prime_factorize(n):
    primes = []
    while n % 2 == 0:
        primes.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            primes.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        primes.append(n)
    return primes

l = len(prime_factorize(N))
i = 0

while 2 ** i < l:
    i += 1
    
print(i)