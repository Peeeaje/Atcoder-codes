import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=" ")


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=" ")


def base_n_to_10(x:int,n:int):
    x = str(x)
    ans=0
    for i in range(1,len(str(x))+1):
        ans+=int(x[-i])*(n**(i-1))
    return ans

def base_10_to_n(x:int,n:int):
    res=''
    while x>0:
        res+=str(x%n)
        x//=n
    return int(res[::-1])


N, K = map(int, input().split())
if N == 0:
    print(0)

else:
    for i in range(K):
        N = base_n_to_10(N, 8)
        N = base_10_to_n(N, 9)
        N = int(str(N).replace("8", "5"))

    print(N)
