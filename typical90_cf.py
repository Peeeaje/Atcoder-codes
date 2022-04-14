N = int(input())
S = input()

if N == 1:
    print(0)
    exit()


def calc_patterns(l: int):
    return l * (l + 1) // 2


run_length = [1]

for i in range(1, N):
    if S[i] == S[i - 1]:
        run_length[-1] += 1
    else:
        run_length.append(1)

ans = calc_patterns(N)
for n in run_length:
    ans -= calc_patterns(n)
print(ans)
