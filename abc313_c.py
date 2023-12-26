n = int(input())
a = list(map(int, input().split()))

avg = sum(a) / n
low = int(avg)
high = low + 1

high_count = 0
low_count = 0
for i in range(n):
    if a[i] <= low:
        low_count += low - a[i]
    elif a[i] >= high:
        high_count += a[i] - high

print(max(high_count, low_count))