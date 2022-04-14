K = int(input())


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


ans = 0
divisors = make_divisors(K)
for i in range(len(divisors)):
    a = divisors[i]
    for j in range(i, len(divisors)):
        b = divisors[j]
        c = K / (a * b)
        if c.is_integer() and c >= b:
            ans += 1
print(ans)
