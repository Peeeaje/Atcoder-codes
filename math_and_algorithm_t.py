import itertools

N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in itertools.combinations(A, 5):
    if sum(i) == 1000:
        ans += 1
print(ans)
