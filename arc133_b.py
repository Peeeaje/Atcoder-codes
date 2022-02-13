import collections


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

d = collections.defaultdict(list)

for i in range(N):
    n = P[i]
    divisors = make_divisors(n)
    for div in divisors:
        d[n].append(div)

for i in range(N):
    n = Q[i]
    print(d[n])
