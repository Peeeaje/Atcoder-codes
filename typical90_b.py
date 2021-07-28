n = int(input())
for i in range(2 ** n):
    temp = str()
    temp_n = 0
    for j in range(n):
        if (i >> j) & 1:
            temp = ")" + temp
            temp_n += 1
        else:
            temp = "(" + temp
            temp_n -= 1

        if temp_n < 0:
            break

    if j == n - 1 and temp_n == 0:
        print(temp)
