N, K = map(int, input().split())


def base_10_to_n(x: int, n: int):
    res = ""
    while x > 0:
        res += str(x % n)
        x //= n
    return int(res[::-1])


if N == 0:
    print(0)
    exit()
for i in range(K):
    N = int(str(N), 8)
    N = base_10_to_n(N, 9)
    N = int(str(N).replace("8", "5"))
print(N)
