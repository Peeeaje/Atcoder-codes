s = set()


def main(t):
    s.add(int(t))
    last = int(t[0])
    for i in range(last + 1, 10):
        main(str(i) + t)


for i in range(0, 10):
    main(str(i))

s = sorted(s)[1:]
n = int(input())
print(s[n - 1])
