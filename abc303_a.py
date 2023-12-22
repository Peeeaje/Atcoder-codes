n = int(input())
d = {"1": "l", "0": "o"}

s = [d[v] if v in d else v for v in input()]
t = [d[v] if v in d else v for v in input()]

if s == t:
    print("Yes")
else:
    print("No")