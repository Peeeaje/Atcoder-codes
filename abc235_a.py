abc = input()
x = abc[0]
y = abc[1]
z = abc[2]

ans = int(x + y + z) + int(y + z + x) + int(z + x + y)
print(ans)
