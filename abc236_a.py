S = input()
a, b = map(int, input().split())
Sa = S[a - 1]
Sb = S[b - 1]

print(S[: a - 1] + Sb + S[a : b - 1] + Sa + S[b:])
