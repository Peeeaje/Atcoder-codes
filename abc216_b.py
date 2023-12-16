N = int(input())
s = set()
for i in range(N):
    name = input()
    if name in s:
        print("Yes")
        exit()
    s.add(name)
print("No")
