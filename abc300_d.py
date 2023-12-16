N = int(input())

# N以下の素数を列挙
def get_primes(N):
    N = int(N ** (1/2)) + 1
    primes = [2]
    for i in range(3, N + 1, 2):
        for p in primes:
            if p * p > i:
                primes.append(i)
                break
            if i % p == 0:
                break
        else:
            primes.append(i)
    return primes

primes = get_primes(N)

ans = 0
for i in range(len(primes)):
    a = primes[i]
    if a * a > N:
        break
    for j in range(i + 1, len(primes)):
        c = primes[j]
        if a * a * c * c > N:
            break
        b = N // (a * a * c * c)
        if a < b < c:
            print(a, b, c)
            ans += int(b)
print(ans)