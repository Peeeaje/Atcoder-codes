S = input()

t = S[0]
for i in range(len(S) - 1):
    if S[i + 1] == S[i]:
        continue
    t += S[i + 1]

if t in ['A', 'AB', "ABC", "AC", "BC", "B", "C"]:
    print("Yes")
else:
    print("No")
