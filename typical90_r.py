import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=" ")


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=" ")


t = from_readline()[0]
L, X, Y = from_readline()
Q = from_readline()[0]


def pos_kanransha(E):
    theta = E * 2 * np.pi / t
    x = 0
    y = -np.sin(theta) * L / 2
    z = (-np.cos(theta) + 1) * L / 2
    return x,y,z

for i in range(Q):
    E = int(input())
    x, y, z = pos_kanransha(E)
    T = [x, y, z]
    B = [x, y, 0]
    C = [X, Y, 0]


    TB = z
    TC = np.sqrt(X**2 + (Y-y)**2 + z**2)
    
    sintheta = TB/TC
    theta = np.arcsin(sintheta)
    ans = theta/np.pi * 180
    print(ans)
