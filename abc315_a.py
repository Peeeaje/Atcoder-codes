S = input()

ans = ""
for s in S:
    if s in set("aiueo"):
        continue
    ans += s

print(ans)