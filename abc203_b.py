N, K = map(int, input().split())

a = sum([i for i in range(100, 100 * N + 1, 100)])
b = sum([i for i in range(1, K + 1, 1)])

print(a * K + b * N)
