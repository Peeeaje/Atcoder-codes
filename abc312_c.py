import bisect


def is_ok(a, b, x):
    ind_a = bisect.bisect_right(a, x)
    ind_b = bisect.bisect_left(b, x)
    return ind_a >= len(b) - ind_b


n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))

left = 0
right = 10 ** 9 + 1
while right - left > 1:
    mid = (left + right) // 2
    if not is_ok(a, b, mid):
        left = mid
    else:
        right = mid

print(left + 1)