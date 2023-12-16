s = list(map(int, input().split(".")))
if 0 <= s[1] <= 2:
    print(str(s[0]) + "-")
elif 3 <= s[1] <= 6:
    print(str(s[0]))
else:
    print(str(s[0]) + "+")
