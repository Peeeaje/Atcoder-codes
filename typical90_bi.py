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


Q = from_readline()[0]
deck = deque()

for i in range(Q):
    tx = list(map(int, input().split()))
    if tx[0] == 1:
        deck.appendleft(tx[1])
    elif tx[0] == 2:
        deck.append(tx[1])
    else:
        print(deck[tx[1]-1])