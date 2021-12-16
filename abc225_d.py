N, Q = map(int, input().split())


# class UnionFind(object):
#     def __init__(self, n=1):
#         self.par = [i for i in range(n)]
#         self.rank = [0 for _ in range(n)]
#         self.size = [1 for _ in range(n)]

#     def find(self, x):
#         """
#         x が属するグループを探索
#         """
#         if self.par[x] == x:
#             return x
#         else:
#             self.par[x] = self.find(self.par[x])
#             return self.par[x]

#     def union(self, x, y):
#         """
#         x と y のグループを結合
#         """
#         x = self.find(x)
#         y = self.find(y)
#         if x != y:
#             if self.rank[x] < self.rank[y]:
#                 x, y = y, x
#             if self.rank[x] == self.rank[y]:
#                 self.rank[x] += 1
#             self.par[y] = x
#             self.size[x] += self.size[y]

#     def is_same(self, x, y):
#         """
#         x と y が同じグループか否か
#         """
#         return self.find(x) == self.find(y)

#     def get_size(self, x):
#         """
#         x が属するグループの要素数
#         """
#         x = self.find(x)
#         return self.size[x]


# unionfind = UnionFind()


class trainlist:
    def __init__(self) -> None:
        self.line = dict()
        self.final = dict()

    def union(self, x, y):
        if 
        self.line[x]


for i in range(Q):
    q = [map(int, input().split())]

    if q[0] == 1:

        pass
        # unionfind.union(q[1], q[2])
    elif q[0] == 2:
        pass
    else:
        pass
# print(unionfind.find(6))
dic = dict()
