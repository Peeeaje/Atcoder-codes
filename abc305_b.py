d = {k: v for k, v in zip("ABCDEFG", [0, 3, 4, 8, 9, 14, 23])}

p, q = input().split()

print(abs(d[p] - d[q]))