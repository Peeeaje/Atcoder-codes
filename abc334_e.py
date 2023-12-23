from collections import defaultdict

MOD = 998244353


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


h, w = map(int, input().split())
S = [list(input()) for _ in range(h)]

uf = UnionFind(h * w)
for i in range(h):
    for j in range(w):
        if S[i][j] == ".":
            continue
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < h and 0 <= nj < w and S[ni][nj] == "#":
                uf.union(i * w + j, ni * w + nj)

cnt = 0
d = {}
set_ = set()
for i in range(h):
    for j in range(w):
        if S[i][j] == ".":
            continue

        if uf.find(i * w + j) not in set_:
            cnt += 1
            set_.add(uf.find(i * w + j))
        d[(i, j)] = uf.find(i * w + j)

ans = 0
for i in range(h):
    for j in range(w):
        if S[i][j] == "#":
            continue
        roots = set()
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            root = d.get((ni, nj), None)
            if root is not None:
                roots.add(root)
        ans += (cnt - len(roots) + 1)
        ans %= MOD

tmp = 0
for i in range(h):
    for j in range(w):
        if S[i][j] == ".":
            tmp += 1
denom = pow(tmp, -1, MOD)
print(ans * denom % MOD)



