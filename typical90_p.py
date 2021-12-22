N = int(input())
ABC = sorted(list(map(int, input().split())))
A = ABC[2]
B = ABC[1]
C = ABC[0]

ans = 100000
for a in range(10000):
    if a * A > N:
        break
    for b in range(10000 - a):
        if a * A + b * B > N:
            break
        if (N - a * A - b * B) % C == 0:
            c = (N - a * A - b * B) // C
            ans = min(ans, a + b + c)

print(ans)
