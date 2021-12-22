N, K = map(int, input().split())
a = list(map(int, input().split()))

dp = [0] * N
cnt = dict()


def return_len_dict(cnt: dict):
    return len([v for v in cnt.values() if v != 0])


for i in range(N):
    for j in range(i, N):
        temp = a[j]
        cnt[temp] += 1
        
