n = int(input())

v = float("inf")

for u in range(0, 101, 5):
    if abs(n - u) < abs(n - v):
        v = u
print(v)

