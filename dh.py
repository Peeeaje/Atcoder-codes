# N = int(input())
# x, y = 0, 0

# for i in range(N):
#     direction = i % 4
#     d = int(input())
#     if direction == 0:
#         x += d
#     if direction == 1:
#         y -= d
#     if direction == 2:
#         x -= d
#     if direction == 3:
#         y += d

# print(x, y)

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

ans = 0
for i in range(N):
    ans += abs(A[i] - B[i])
print(ans)