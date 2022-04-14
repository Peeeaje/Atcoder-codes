N = int(input())


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


primes = prime_factorize(N)
ans = 0
while 2 ** ans < len(primes):
    ans += 1
print(ans)