import collections

a, N = map(int, input().split())
d = collections.defaultdict(int)
X = set([1])


def rotate(a):
    a = str(a)
    return int(a[-1] + a[:-1])


# def multiply(a, x):
#     l = []
#     for x in X:
#         l.append(x * a)
#     return l


def process(a, X):
    new_X = set([])
    for x in X:
        if x * a >= 10 ** len(str(N)):
            if x >= 10 and x % 10 != 0:
                if d[rotate(x)] != 1:
                    new_X.add(rotate(x))
                    d[rotate(x)] = 1
                else:
                    continue
        else:
            if x >= 10 and x % 10 != 0:
                if d[rotate(x)] != 1:
                    new_X.add(rotate(x))
                    d[rotate(x)] = 1

                if d[x * a] != 1:
                    new_X.add(x * a)
                    d[x * a] = 1
            else:
                if d[x * a] != 1:
                    new_X.add(x * a)
                    d[x * a] = 1

    return new_X


i = 1
while len(X) != 0:
    X = process(a, X)
    if N in X:
        print(i)
        exit()
    i += 1

print(-1)
