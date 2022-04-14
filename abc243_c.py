import collections

N = int(input())

min_dict = collections.defaultdict(lambda: float("inf"))
max_dict = collections.defaultdict(lambda: -float("inf"))

for i in range(N):
    x, y = map(int, input().split())
    min_int = min_dict[y]
    if x < min_int:
        min_dict[y] = x
    max_int = max_dict[y]
    if x > max_int:
        max_dict[y] = x

S = input()
