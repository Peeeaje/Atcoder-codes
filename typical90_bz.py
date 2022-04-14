import collections

N, M = map(int, input().split())
count_dict = collections.defaultdict(int)
for i in range(M):
    a, b = map(int, input().split())
    larger = max(a, b)
    count_dict[larger] += 1

print(sum([1 for key, val in count_dict.items() if val == 1]))
