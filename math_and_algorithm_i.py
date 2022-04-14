import numpy as np

N, S = map(int, input().split())
A = list(map(int, input().split()))

temp = set([0])
for a in A:
    temp = temp | set([value + a for value in temp])

if S in temp:
    print("Yes")
else:
    print("No")

