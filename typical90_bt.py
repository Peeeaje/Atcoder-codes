import sys
from collections import deque

import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=" ")


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=" ")


site = list()
H, W = from_readline()
for i in range(H):
    site.append(list(input()))
#     H, W = 2,2
# site = [[".", ".",], [".", ".",]]
s = [0, 1]

visited = [[False] * W for _ in range(H)]
dist = [[-1] * W for _ in range(H)]
stack = deque()


def dfs(s):
    # initialize for first node
    start = s
    stack.append(s)
    step = 1
    dist[s[0]][s[1]] = step

    while len(stack):
        # process node
        step += 1
        s = stack.pop()
        visited[s[0]][s[1]] = True
        dist[s[0]][s[1]] = step

        # append next pathes to stack
        for a in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            x = s[0] + a[0]
            y = s[1] + a[1]

            if 0 <= x < H and 0 <= y < W:
                if visited[x][y] == False and site[x][y] != "#":
                    stack.append([x, y])

                # process goal
                if [x, y] == start and step >= 4:
                    return visited, "Yes"
                    quit()

        print(visited)
    return visited, "No"


print(dfs(s))
