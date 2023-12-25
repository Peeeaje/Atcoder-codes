def judge(s):
    for i in range(3):
        for j in range(3):
            if s[i][j] != "#":
                return False
            if s[-1-i][-1-j] != "#":
                return False
    for i in range(4):
        for j in range(4):
            if i != 3 and j != 3:
                continue
            if s[i][j] == "#":
                return False
            if s[-1-i][-1-j] == "#":
                return False
    return True


n, m = map(int, input().split())
S = [list(input()) for _ in range(n)]

for i in range(n - 9 + 1):
    for j in range(m - 9 + 1):
        if judge([s[j:j+9] for s in S[i:i+9]]):
            print(i + 1, j + 1)
