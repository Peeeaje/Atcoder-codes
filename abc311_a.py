n = int(input())
s = input()

a = False
b = False
c = False

for i in range(n):
    if s[i] == "A":
        a = True
    elif s[i] == "B":
        b = True
    elif s[i] == "C":
        c = True

    if a and b and c:
        print(i + 1)
        exit()