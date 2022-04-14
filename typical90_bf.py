convert_dict = {}
for i in range(10**5):
    convert_dict[i] = (sum(map(int, list(str(i)))) + i) % 10**5

N, K = map(int, input().split())
initial_N = N
used_numbers = [0 for _ in range(10**5)]
loop = 10**20

i = 0
while i < K:
    N = convert_dict[N]
    i += 1

    if loop == 10**20 and used_numbers[N]:
        loop = i - used_numbers[N]
        K -= ((K - i) // loop) * loop
    used_numbers[N] = i

print(N)
