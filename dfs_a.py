import sys
import numpy as np
from collections import deque

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=" ")


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=" ")


H, W = from_readline()
c = list()
for i in range(H):
    c.append(list(input()))



for i in range(H):
    if "s" in c[i]:
        s = [i, c[i].index("s")]
        
for i in range(H):
    if "g" in c[i]:
        g = [i, c[i].index("g")]


visited = [[False] * W for _ in range(H)]
dist = [[-1] * W for _ in range(H)]
stack = deque()

def dfs(s):
    # initialize for first node
    stack.append(s)
    dist_temp = 1
    dist[s[0]][s[1]] = dist_temp
    
    while len(stack):
        # process node
        s = stack.pop()
        visited[s[0]][s[1]] = True
        
        # process goal
        if s == g:
            return "Yes"
            quit()

        # append next pathes to stack
        for a in [[1,0], [-1,0], [0, 1], [0, -1]]:
            x = s[0] + a[0]
            y = s[1] + a[1]

            if 0 <= x < H and 0 <= y < W and visited[x][y] == False:
                if c[x][y] != "#":
                    stack.append([x, y])
                    dist_temp += 1
                    dist[x][y] = dist_temp
    return "No"



print(dfs(s))
