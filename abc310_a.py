n, p, q = map(int, input().split())
m = min(list(map(int, input().split())))

print(min(p, q + m))
