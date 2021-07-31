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
    x_k, y_k, z_k = pos_kanransha(E)
    T = [x_k, y_k, z_k]
    B = [x_k, y_k, 0]
    C = [X, Y, 0]

    print(T, B, C)

    TB = z_k
    BC = np.sqrt((x_k)**2 + (Y-y_k)**2 + (z_k)**2)
    
    if E == 0:
        ans = 0
    else:
        # costheta = (TB**2 + TC**2 - BC**2)/(2*TB*TC)
        # print(costheta)
        # theta = np.arccos(costheta)
        tantheta = BC/TB
        theta = np.arctan(tantheta)
        ans = theta/np.pi * 180
    print(ans)
