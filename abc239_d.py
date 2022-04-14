from tempfile import tempdir


A, B, C, D = map(int, input().split())

prime_range = [A + C, B + D]

def sieve(n):
    is_prime = [True for _ in range(n+1)]
    is_prime[0] = False

    for i in range(2, n+1):
        if is_prime[i-1]:
            j = 2 * i
            while j <= n:
                is_prime[j-1] = False
                j += i
    table = [ i for i in range(1, n+1) if is_prime[i-1]]
    return is_prime, table


temp = sieve(B + D)[1]
prime_list = []

for i in temp:
    if i < A + C:
        continue
    prime_list.append(i)


for t in range(A, B+1):
    l = set([*range(t + C, t + D + 1)])

    f = 0
    for p in prime_list:
        if p not in l:
            f += 1

    if f == len(prime_list):
        print("Takahashi")
        exit()

print("Aoki")