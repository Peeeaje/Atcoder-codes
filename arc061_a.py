def calc_sum_from_index_list(number: str, index_list: list):
    sum_ = 0
    s = 0
    index_list.append(len(number))
    if len(index_list) == 0:
        return int(number)

    for i in index_list:
        # i >= 1
        sum_ += int(number[s:i])
        s = i
    return sum_


N = input()

len_n = 2 ** (len(N) - 1)

ans = 0
for i in range(len_n):
    ind_list = []
    for j in range(len(N) - 1):
        if i & 1 << j:
            ind_list.append(j + 1)

    ans += calc_sum_from_index_list(N, ind_list)
print(ans)
