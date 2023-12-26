from itertools import permutations


m = int(input())
S = [list(input()) for _ in range(3)]
possible = set()
for i in range(10):
    if str(i) not in S[0]:
        continue
    if str(i) not in S[1]:
        continue
    if str(i) not in S[2]:
        continue
    possible.add(i)

if len(possible) == 0:
    print(-1)
    exit()

ans = float("inf")
for perm in permutations(S, 3):
    s1, s2, s3 = perm

    for i in possible:
        j = 0
        while True:
            if s1[j % m] == str(i):
                j += 1
                break
            j += 1
        while True:
            if s2[j % m] == str(i):
                j += 1
                break
            j += 1
        while True:
            if s3[j % m] == str(i):
                break
            j += 1
        ans = min(ans, j)

print(ans)
