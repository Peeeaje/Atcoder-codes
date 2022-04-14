import collections

N = int(input())
S = input()

left = collections.deque([0])
right = collections.deque()


for i in range(N):
    s = S[i]
    if s == 'L':
        right.appendleft(left.pop())
        left.append(i + 1)
    if s == "R":
        left.append(i + 1)
        
print(" ".join(map(str, left)) + " " + " ".join(map(str, right)))