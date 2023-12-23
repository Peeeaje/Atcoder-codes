def is_kaibun(s):
    for i in range(len(s) // 2):
        if s[i] != s[-1 - i]:
            return False
    return True


n = int(input())
l = [input() for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        s = l[i] + l[j]
        if is_kaibun(s):
            print("Yes")
            exit()

print("No")
