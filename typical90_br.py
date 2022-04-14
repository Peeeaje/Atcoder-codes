N = int(input())
x_list = []
y_list = []

for i in range(N):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)
med_x = sorted(x_list)[N//2]
med_y = sorted(y_list)[N//2]

ans = 0
for x in x_list:
    ans += abs(x - med_x)
for y in y_list:
    ans += abs(y - med_y)
print(ans)
