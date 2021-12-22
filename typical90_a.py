def check_able_to_cut(K, A, ans):
    l = [A[0]]
    for i in range(1, len(A)):
        l.append(A[i] - A[i - 1])

    temp = 0
    cut = 0
    for i in l:
        temp += i
        if temp >= ans:
            temp = 0
            cut += 1

        if cut == K + 1:
            return True
    return False


N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))
A.append(L)

ans = N


def is_ok(mid):
    # 条件を満たすかどうか？問題ごとに定義
    return check_able_to_cut(K, A, mid)


def meguru_bisect(ng, ok):
    """
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    """
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid) is True:
            ng = mid
        else:
            ok = mid

    return ng


print(meguru_bisect(-1, L + 1))
