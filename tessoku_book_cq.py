n, s = map(int, input().split())
a = list(map(int, input().split()))

l = [False] * (s + 1)
l[0] = True
S = [[] for _ in range(s + 1)]

for i in range(n):
    a_i = a[i]
    slided = [False] * a_i + l[:s + 1 - a_i]
    for j in range(1, s + 1):
        l[j] |= slided[j]
        if l[j] and not S[j]:
            S[j] = S[j - a_i] + [i + 1]

if l[s]:
    print(len(S[s]))
    print(*S[s])

else:
    print(-1)