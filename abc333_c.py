from itertools import product

n = int(input())

l = [int('1' * v) for v in range(1, 13)]
ll = set()
for i in range(len(l)):
    for j in range(len(l)):
        for k in range(len(l)):
            ll.add(l[i] + l[j] + l[k])
print(sorted(ll)[n - 1])