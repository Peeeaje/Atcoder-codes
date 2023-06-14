N, K = map(int, input().split())
a = list(map(int, input().split()))

common = K // N
remainder = K % N
sorted_a = sorted(a)
sorted_a = [0] + sorted_a
threshold = sorted_a[remainder]
for val in a:
    if val <= threshold:
        print(common + 1)
    else:
        print(common)
