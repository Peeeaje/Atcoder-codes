N = int(input())
A = list(map(int, input().split()))

temp2 = [0]
temp1 = 0

for a in A:
    temp1 = (temp1 + a) % 360
    temp2.append(temp1)

temp2.sort()
temp2.append(360)

ans = []

for i in range(len(temp2) - 1):
    ans.append(temp2[i + 1] - temp2[i])
print(max(ans))
