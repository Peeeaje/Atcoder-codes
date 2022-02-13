import itertools

N = int(input())
A = []
for i in range(2 * N - 1):
    temp = [0 for _ in range(i + 1)]
    temp.extend(list(map(int, input().split())))
    A.append(temp)

for n in itertools.combinations(range(2 * N), 2):
    print(n)
# for i in range(2 * N - 1):
#     for j in range(i + 1, 2 * N):
        