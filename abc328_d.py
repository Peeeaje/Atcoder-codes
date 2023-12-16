from collections import deque

S = input()
if len(S) < 3:
    print(S)
    exit()

T = deque(S[:3])
if S[:3] == 'ABC':
    for _ in range(3):
        T.pop()

for s in S[3:]:
    if s == 'C' and len(T) >= 2 and T[-2] == 'A' and T[-1] == 'B':
        T.pop()
        T.pop()
    else:
        T.append(s)

print(''.join(T))

