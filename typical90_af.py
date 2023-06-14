import itertools

N = int(input())
A = list()
B = set()
for i in range(N):
    A.append(list(map(int, input().split())))

M = int(input())
for i in range(M):
    temp_input = list(map(int, input().split()))
    B.add(tuple([value - 1 for value in temp_input]))


def can_run(runners):
    for i in range(0, N):
        if i > 0:
            runner_a = runners[i - 1]
            runner_b = runners[i]
            if (runner_a, runner_b) in B or (runner_b, runner_a) in B:
                return False
    return True


def calc_distance(runners):
    distance = 0
    for i in range(0, N):
        distance += A[runners[i]][i]
    return distance


ans = 10**20
for runners in itertools.permutations(range(N)):
    if can_run(runners):
        temp_ans = calc_distance(runners)
        ans = min(ans, temp_ans)

if ans == 10**20:
    print(-1)
else:
    print(ans)
