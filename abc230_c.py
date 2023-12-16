N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

ans = [["."] * (S - R + 1) for _ in range(Q - P + 1)]

for k in range(max(P - A, R - B), min(Q - A, S - B) + 1):
    try:
        ans[k + A - 1 - P][k + B - 1 - R] = "#"
    except:
        pass

for k in range(max(P - A, B - S), min(Q - A, B - R) + 1):
    print(k)
    try:
        ans[A + k - 1 - P][B - k - 1 - R] = "#"
        print(k + A, -k + B)
    except:
        pass
print(ans)
