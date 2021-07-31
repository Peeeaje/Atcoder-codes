N = int(input())
A, B, C = map(int, input().split())
ans = 10 ** 9

for a in range(10000):
    a_sum = A * a

    if a_sum > N:
        break

    for b in range(10000 - a):
        b_sum = B * b

        if a_sum + b_sum > N:
            break

        if (N - a_sum - b_sum) % C == 0:
            ans = min(ans, a + b + (N - a_sum - b_sum) // C)

print(ans)