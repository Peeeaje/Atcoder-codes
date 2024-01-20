def base_n(num_10,n):
    str_n = ''
    while num_10:
        if num_10%n>=10:
            return -1
        str_n += str(num_10%n)
        num_10 //= n
    return int(str_n[::-1])


n = int(input())
if n == 1:
    print(0)
else:
    n = base_n(n - 1, 5)
    print(n * 2)
