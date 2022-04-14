# def f(x):
#     return x - 10 ** (len(str(x)) - 1) + 1

N = int(input())
L = len(str(N))


def sum_under_L(L):
    temp = []
    for i in range(1, L):
        temp.append((9 * 10 ** (i - 1) + 1) * 9 * 10 ** (i - 1) // 2)
    return sum(temp)


def sum_L(L, N):
    temp = []
    end = N
    for i in range(1, L):
        temp.append((end + 1) * 9 * 10 ** (i - 1) // 2)
    return sum(temp)


# print(sum_under_L(L))

temp = N - 10 ** (L - 1)
print((sum_under_L(L) + (temp + 1) * (temp + 2) // 2) % 998244353)
