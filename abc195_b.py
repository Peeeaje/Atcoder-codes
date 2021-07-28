import sys
import numpy as np
import math

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=" ")


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=" ")


A, B, W = map(int, read().split())

BTM = math.ceil(W * 1000 / B)
UP = math.floor(W * 1000 / A)

if (A * BTM <= W * 1000 <= B * BTM) and (A * UP <= W * 1000 <= B * UP):
    print(BTM, UP)
    exit()

print("UNSATISFIABLE")