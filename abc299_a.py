
N = int(input())
S = input()

a, b, c = -1, -1, -1
for i in range(N):
    if S[i] == '|' and a == -1:
        a = i
    if S[i] == '*':
        b = i
    if S[i] == '|' and a != -1:
        c = i

if a < b < c:
    print('in')
else:
    print('out')
