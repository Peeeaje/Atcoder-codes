import collections

N = int(input())
d = {
    1: [1, 2],
    2: [1, 2, 3],
    3: [2, 3, 4],
    4: [3, 4, 5],
    5: [4, 5, 6],
    6: [5, 6, 7],
    7: [6, 7, 8],
    8: [7, 8, 9],
    9: [8, 9],
}

dp = [{} for _ in range(N)]
dp[0] = {
    1: 1,
    2: 1,
    3: 1,
    4: 1,
    5: 1,
    6: 1,
    7: 1,
    8: 1,
    9: 1,
}


def return_next(dp_i):
    next_dp = collections.defaultdict(int)
    for k, mul in dp_i.items():
        if k == 1:
            next_dp[k] += mul
            next_dp[k + 1] += mul
        elif k == 9:
            next_dp[k - 1] += mul
            next_dp[k] += mul
        else:
            next_dp[k - 1] += mul
            next_dp[k] += mul
            next_dp[k + 1] += mul
    return next_dp


for i in range(1, N):
    dp[i] = return_next(dp[i - 1])
ans = 0
for k, v in dp[-1].items():
    ans += v
print(ans % 998244353)
