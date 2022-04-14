import collections

N = int(input())
A = list(map(int, input().split()))

print([value for value, fre in collections.Counter(A).most_common()][-1])
