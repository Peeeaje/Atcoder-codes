n = int(input())

l = len(str(n))
m = 10 ** (l - 3)
if n <= 999:
    print(n)
else:
    print(int((n // m) * m))
