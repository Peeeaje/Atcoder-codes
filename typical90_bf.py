def sum_int(i: int):
    i = str(i)
    temp = 0
    for j in range(len(i)):
        temp += int(i[j])
    return temp


N, K = map(int, input().split())
seen = [-1] * 10 ** 5

dic = {}
for i in range(10 ** 5):
    dic[i] = (i + sum_int(i)) % (10 ** 5)

n = N
loop = 10 ** 19

i = 0
while i < K:
    seen[n] = i
    n = dic[n]
    i += 1

    if seen[n] != -1:
        loop = i - seen[n]
        i += loop * ((K - i) // loop)
        seen = [-1] * 10 ** 5


print(n)
