from itertools import permutations

S, K = input().split()
S = sorted(S)
K = int(K)
memo = set()
d_v = 0

for ind, s in enumerate(permutations(S)):
    if s in memo:
        d_v += 1
    memo.add(s)

    if ind - d_v == K - 1:
        print("".join(s))
        exit()
