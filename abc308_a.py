s = list(map(int, input().split()))

for i in range(len(s)):
    if s[i] % 25 != 0:
        print("No")
        exit()
    if s[i] < 100 or 675 < s[i]:
        print("No")
        exit()
    if i > 0 and s[i] < s[i-1]:
        print("No")
        exit()

print("Yes")

