N = int(input())
S = input()

atcoder = "atcoder"
dp = [[0] * 7 for i in range(N)]


def return_prev_string(string):
    index = atcoder.index(string)
    return atcoder[index - 1]


for i in range(len(S)):
    dp[i] = dp[i - 1]
    s = S[i]
    if (i == 0 and s != "a") or s not in atcoder:
        continue

    if s == "a":
        dp[i][0] += 1

    else:
        index = atcoder.index(s)
        dp[i][index] += dp[i - 1][atcoder.index(return_prev_string(s))]

print(dp[-1][-1] % (10 ** 9 + 7))
