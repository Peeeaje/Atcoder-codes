from collections import defaultdict

n = int(input())

tx = []
for e in range(n):
    t, x = map(int, input().split())
    tx.append((t, x))

n_portion = []
ans = []
need = defaultdict(int)
for i in range(n - 1, -1, -1):
    t, x = tx[i]
    if t == 1:
        if need[x] > 0:
            need[x] -= 1
            ans.append(1)
            n_portion.append(1)
        else:
            ans.append(0)
    else:
        need[x] += 1
        n_portion.append(-1)

if any([e > 0 for e in need.values()]):
    print(-1)
    exit()

n_portion = (n_portion+[0])[::-1]
tmp = 0
for i in range(len(n_portion)):
    tmp += n_portion[i]
    n_portion[i] = tmp

ans = ans[::-1]
print(max(n_portion))
print(*ans)
