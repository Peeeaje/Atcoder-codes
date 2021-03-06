N = int(input())
A = list(map(int, input().split()))
A = sorted(A)
Q = int(input())
MIN = min(A)
MAX = max(A)


def is_ok(mid):
    # 条件を満たすかどうか？問題ごとに定義
    return A[mid] >= B


def meguru_bisect(ng, ok):
    """
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    """
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


for i in range(Q):
    B = int(input())
    ind = meguru_bisect(0, N) - 1
    ans = abs(B - A[ind])
    if ind != N - 1:
        ans = min(ans, abs(B - A[ind + 1]))
    print(ans)
