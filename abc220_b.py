import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=" ")


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=" ")

K, A, B = from_read()

def base_n_to_10(x:int,n:int):
    x = str(x)
    ans=0
    for i in range(1,len(str(x))+1):
        ans+=int(x[-i])*(n**(i-1))
    return ans

A = base_n_to_10(A, K)
B = base_n_to_10(B, K)

print(A*B)