# O(EV)
def bellman_ford(s):
    d = [float("inf")] * n  # 各頂点への最小コスト
    d[s] = 0  # 自身への距離は0
    for i in range(n):
        update = False  # 更新が行われたか
        for x, y, z in g:
            if d[y] > d[x] + z:
                d[y] = d[x] + z
                update = True
        if not update:
            break
        # 負閉路が存在
        if i == n - 1:
            return -1
    return d


n, w = map(int, input().split())
H = list(map(int, input().split()))
g = []
for _ in range(w):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    if H[x] >= H[y]:
        g.append([x, y, -H[x] + H[y]])
        g.append([y, x, 2 * (H[x] - H[y])])
    else:
        g.append([x, y, 2 * (H[y] - H[x])])
        g.append([y, x, -H[y] + H[x]])

    # z = H[x - 1] - H[y - 1]
    # x, y, z = [int(x) for x in input().split()] # 始点,終点,コスト
    # g.append([x, y, z])
    # g.append([y, x, z]) # 有向グラフでは削除
print(abs(min(bellman_ford(0))))
