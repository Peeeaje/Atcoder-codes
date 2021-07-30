N = int(input())

for i in range(2 ** N):
    b_i = bin(i)
    s = str()
    temp = 0

    for j in range(N):
        if ((i >> j) & 1):
            temp += 1
            s += ")"
        else:
            temp -= 1
            s += "("
        if temp < 0:
            break
            
    if temp == 0:
        print(s[::-1])