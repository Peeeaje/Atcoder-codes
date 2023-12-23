n = int(input())
S = [list(input()) for _ in range(n)]

def sort_func(x):
    index, cnt = x
    return (-cnt, index)


win_list = []
for i in range(n):
    cnt = 0
    for s in S[i]:
        if s == "o":
            cnt += 1
    win_list.append((i, cnt))

print(win_list)
win_list = sorted(win_list, key=sort_func)
print(win_list)