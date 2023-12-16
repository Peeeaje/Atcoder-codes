S = input()
T = input()

d = {}
a = "abcdefghijklmnopqrstuvwxyz"
for i in range(26):
    d[a[i]] = i + 1

diff = (d[T[0]] - d[S[0]]) % 26
for i in range(1, len(S)):
    if (d[T[i]] - d[S[i]]) % 26 != diff:
        print("No")
        exit()

print("Yes")
