import re

S = "10000(10000(10000(2000(ab)500(dz)c200h)2mu3000(fpr)))"
temp = ""
flag = 0
l = []
for i in range(len(S)):
    if S[i] in set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]):
        temp += S[i]
        flag = 1

    elif flag == 1 and S[i] not in set(
        ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    ):
        l.append(int(temp))
        l.append(S[i])
        temp = ""
        flag = 0
    elif S[i] == ")":
        l.append(S[i])

    else:
        l.append(1)
        l.append(S[i])


def calc(n, l):
    for i in range(len(l)):

        if type(l[i]) == int:
            l[i] *= n
    return l


start = []
temp = []
n = []

i = 0
while len(l) > i:
    if l[i] == "(":
        n.append(l[i - 1])
        start.append(i)
    elif l[i] == ")":
        popped = start.pop()
        l[popped - 1 : i + 1] = calc(n.pop(), l[popped + 1 : i])
        i -= 3
    i += 1

c = {}
for val in list("abcdefghijklmnopqrstuvwxyz"):
    c[val] = 0

for i in range(0, len(l), 2):
    num = l[i]
    val = l[i + 1]
    c[val] += num

for val in list("abcdefghijklmnopqrstuvwxyz"):
    print(str(val) + " " + str(c[val]))
