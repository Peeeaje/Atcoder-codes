import collections


def process(l1: list, l2: list):
    l = list()
    for former in l1:
        for latter in l2:
            if former % latter == 0:
                l.append(former // latter)
    return l


N, X = map(int, input().split())
former = [X]
for i in range(N):
    latter = list(map(int, input().split()))[1:]
    former = process(former, latter)

print(collections.Counter(former)[1])
