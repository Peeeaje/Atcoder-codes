def is_kaibun(s):
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            return False
    return True

S = input()
n = len(S)

ans = -1
for i in range(n):
    for j in range(i, n):
        if is_kaibun(S[i:j + 1]):
            ans = max(ans, j - i + 1)

print(ans)