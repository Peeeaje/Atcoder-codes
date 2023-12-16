import bisect

n = int(input())
a = list(map(int, input().split()))
sum_a = sum(a)


sorted_a = sorted(a)
cumsum = [0] * (n + 1)
for i in range(n):
    cumsum[i + 1] = cumsum[i] + sorted_a[i]

ans = []
for i in range(n):
    index = bisect.bisect_right(sorted_a, a[i])
    ans.append(sum_a - cumsum[index])
print(*ans)