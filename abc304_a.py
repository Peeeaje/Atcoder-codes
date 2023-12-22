n = int(input())
l = []
ind = float('inf')
v = float('inf')

for i in range(n):
    name, t = input().split()
    l.append([name, int(t)])

    if v > int(t):
        ind = i
        v = int(t)


for i in range(n):
    tmp = (ind + i) % n
    print(l[tmp][0])