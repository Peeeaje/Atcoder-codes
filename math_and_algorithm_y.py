N = int(input())
A = sum(list(map(int, input().split())))
B = sum(list(map(int, input().split())))

ans = (A + B * 2) / 3
print(ans)
