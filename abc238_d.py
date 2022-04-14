# T = int(input())
# for i in range(T):
#     a, s = map(int, input().split())
#     # print(a, s)
#     # print(bin(a), bin(s))

s = 100
print(bin(55))
for i in range(1, s):
    l = s - i
    print(bin(i)[2:], bin(l)[2:], bin(i & l)[2:])

