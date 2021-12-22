import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=" ")


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=" ")


def next_squares(x, y):
    temp = [[x + 0, y + 1], [x + 0, y - 1], [x + 1, y + 0], [x - 1, y + 0]]
    for x, y in temp:
        if x <= 0 or x > H or y <= 0 or y > W or array[x][y] == 0:
            continue
        yield slice_to_index(x, y)


def slice_to_index(x, y):
    return y * (H + 1) + x


class UnionFind(object):
    def __init__(self, n=1):
        self.par = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, x):
        """
        x が属するグループを探索
        """
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        """
        x と y のグループを結合
        """
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.par[y] = x
            self.size[x] += self.size[y]

    def is_same(self, x, y):
        """
        x と y が同じグループか否か
        """
        return self.find(x) == self.find(y)

    def get_size(self, x):
        """
        x が属するグループの要素数
        """
        x = self.find(x)
        return self.size[x]


H, W = from_readline()
array = np.zeros((H + 1, W + 1))

Q = from_readline()[0]
union_find = UnionFind((H + 1) * (W + 1))

for i in range(Q):
    q = from_readline()

    if q[0] == 1:
        array[q[1]][q[2]] = 1
        node = slice_to_index(q[1], q[2])
        for comp_node in next_squares(q[1], q[2]):
            union_find.union(node, comp_node)

    else:
        ra, ca, rb, cb = q[1], q[2], q[3], q[4]
        if array[ra, ca] == array[rb, cb] == 1:
            if union_find.is_same(slice_to_index(ra, ca), slice_to_index(rb, cb)):
                print("Yes")
            else:
                print("No")
        else:
            print("No")

