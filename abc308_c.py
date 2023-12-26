from functools import cmp_to_key


def sort_method(a, b):
    a_i, a_a, a_b = a
    b_i, b_a, b_b = b

    x = a_a * (b_a + b_b)
    y = b_a * (a_a + a_b)
    if x > y:
        value = -1
    elif x < y:
        value = 1
    else:
        value = 0
    return value


n = int(input())
l = []

for i in range(n):
    a, b = map(int, input().split())
    l.append((i, a, b))


l.sort(key=cmp_to_key(sort_method))
ans = [x[0] + 1 for x in l]
print(*ans)
