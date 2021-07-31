N = int(input())
A = list(map(int, input().split()))
A.sort()
Q = int(input())

def is_ok(mid):
    if A[mid] > B:
        return True
    else:
        return False
    pass


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
    B = int(input())
    ind = meguru_bisect(-1, N)
    if ind == 0:
        ans = abs(B-A[ind])
    elif ind == N:
        ans = abs(B-A[ind-1])
    else:
        ans = min(abs(B - A[ind-1]), abs(B - A[ind]))
    print(ans)
    