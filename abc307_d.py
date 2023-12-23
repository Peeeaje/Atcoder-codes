from collections import deque

n = int(input())
S = list(input())
q = deque()

ans = ""
for i in range(n):
    s = S[i]
    ans += s
    if s =="":
        q.append(i)
    if q and s ==")":
        ans =
