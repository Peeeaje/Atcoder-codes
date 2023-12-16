N, K = map(int, input().split())
S = input()

alp = 'abcdefghijklmnopqrstuvwxyz'
indexes = [[-1] * N for _ in range(26)]
for a in alp:
    l = 0
    for i, s in enumerate(S):
        if s == a:
            indexes[ord(a) - ord('a')][l:i + 1] = [i] * (i - l + 1)
            l = i

print(indexes)

ans = ''
last = -1
for i in range(K):
    for a in alp:
        if indexes[ord(a) - ord('a')][i] != -1 and indexes[ord(a) - ord('a')][i] + K - 1 < N and indexes[ord(a) - ord('a')][i] > last:
            ans += a
            last = indexes[ord(a) - ord('a')][i]
            break

print(ans)