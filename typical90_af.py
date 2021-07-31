import itertools

N = int(input())
A = list()

for i in range(N):
    A.append(list(map(int, input().split())))

M = int(input())
X = set()

for i in range(M):
    X.add(tuple(map(int, input().split())))

temp = [i+1 for i in range(N)]

ans = 10 ** 9

for i in itertools.permutations(temp):
    ans_temp = 0
    f = 0
    run_list = i

    for j in range(N-1):
        if (run_list[j], run_list[j+1]) in X or (run_list[j+1], run_list[j]) in X:
            f = 1
            break
    
    if f == 0:
        for dis in range(N):
            per = run_list[dis] - 1
            ans_temp += A[per][dis]
    
        ans = min(ans, ans_temp)

print(ans if ans != 10 ** 9 else -1)

