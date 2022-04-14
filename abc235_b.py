N = int(input())
H = list(map(int, input().split()))

temp = -1
for h in H:
    if h > temp:
        temp = h

    else:
        print(temp)
        exit()
print(temp)
