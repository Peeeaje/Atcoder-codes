import copy

N = int(input())
A = list(map(int, input().split()))

pattern = [0] * 10
pattern[A[0]] += 1

dict = [[0, 0] * 10 for i in range(10)]

for i in range(10):
    for j in range(10):
        dict[i][j] = [(i + j) % 10, i * j % 10]

dp_A = [0] * 10
dp_A[A[0]] += 1

for n in range(N - 1):
    dp_B = [0] * 10
    temp = [dict[i][A[n + 1]] for i in range(10)]
    for i in range(len(temp)):
        if temp[i]:
            a, b = temp[i]

            dp_B[a] += dp_A[i]
            dp_B[b] += dp_A[i]
    dp_A = copy.copy(dp_B)
    
for i in dp_B:
    print(i % 998244353)
