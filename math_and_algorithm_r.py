import collections

N = int(input())
A = list(map(int, input().split()))

c = collections.Counter(A)

ans = c[200] * c[300] + c[100] * c[400]
print(ans)
