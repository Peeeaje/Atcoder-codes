import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=" ")


def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=" ")


N, L = from_readline()
K = from_readline()[0]
A = from_readline()
A_ = np.diff(np.hstack([0, A, L]))


def is_ok(mid):
    # 条件を満たすかどうか？問題ごとに定義
    sum_len = 0
    cut_cnt = 0

    for i in range(len(A_)):
        sum_len += A_[i]
        if sum_len >= mid:
            sum_len = 0
            cut_cnt += 1

    if cut_cnt >= K+1:
        return True
    else:
        return False


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


print(meguru_bisect(A[-1]+1, -1))