s = input()
t = input()

d = {v: k for k, v in enumerate("ABCDE")}
s1 = d[s[0]]
s2 = d[s[1]]
t1 = d[t[0]]
t2 = d[t[1]]


ls = min(abs(s1 - s2), abs(s2 - s1 + 5), abs(s1 - s2 + 5))
lt = min(abs(t1 - t2), abs(t2 - t1 + 5), abs(t1 - t2 + 5))

if ls == lt:
    print("Yes")
else:
    print("No")
