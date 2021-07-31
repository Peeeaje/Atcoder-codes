N = int(input())

l = set()
for i in range(1, N + 1):
    S = input()

    if S in l:
        pass
    else:
        l.add(S)
        print(i)