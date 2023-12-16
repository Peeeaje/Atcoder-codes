h, w = map(int, input().split())
S = [list(input()) for _ in range(h)]


def check(a, b):
    if 0 <= a - 2 and a + 2 < h:
        print(S[a - 2 : a + 2])

for i in range(h):
    for j in range(w):
        print(check(i, j))