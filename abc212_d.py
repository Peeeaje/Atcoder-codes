import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=" ")


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=" ")


hukuro = np.array([])
Q = from_readline()[0]

def is_ok(mid):
    if hukuro[mid] < query[1]:
        return False
    else:
        return True


def meguru_bisect(ng, ok):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

for i in range(Q):
    query = from_readline()
    if query[0] == 1:
        if len(hukuro) == 0:
            hukuro = np.append(hukuro, query[1])
        else:
            ind = meguru_bisect(len(hukuro), -1)
            hukuro = np.insert(hukuro, ind, query[1])
    if query[0] == 2:
        hukuro += query[1]
    if query[0] == 3:
        print(int(hukuro[-1]))
        hukuro = hukuro[:-1]
