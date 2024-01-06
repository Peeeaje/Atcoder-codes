n = int(input())

ans = [[-1] * n for _ in range(n)]
ans[0][0] = 1
dir = (1, 0)
cur = [0, 0]

dir_d = {
        (1, 0): (0, 1),
        (0, 1): (-1, 0),
        (-1, 0): (0, -1),
        (0, -1): (1, 0)
        }

for i in range(1, n ** 2 - 1):
    next_cand = [cur[0] + dir[0], cur[1] + dir[1]]
    if next_cand[0] < 0 or next_cand[0] >= n or next_cand[1] < 0 or next_cand[1] >= n or ans[next_cand[0]][next_cand[1]] != -1:
        dir = dir_d[dir]
        next = [cur[0] + dir[0], cur[1] + dir[1]]
    else:
        next = next_cand

    ans[next[0]][next[1]] = i + 1
    cur = next

ans[n // 2][n // 2] = 'T'

for row in ans:
    print(*row)
