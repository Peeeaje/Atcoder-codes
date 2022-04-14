N = int(input())
l = []
for i in range(N):
    l.append(sum(list(map(int, input().split()))))
ans = 1
for val in l:
    ans = ans * val % (10 ** 9 + 7)
print(ans)
