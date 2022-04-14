S = input()

if set(list(S)) == {"a"}:
    print("Yes")

else:
    last = -1
    while S[last] == "a":
        last -= 1

    start = 0
    while S[start] == "a":
        start += 1

    if abs(last + 1) - abs(start) > 0:
        S = S[: last + start] + S[last + start]

    for i in range(len(S) // 2):
        if S[i] != S[-i - 1]:
            print("No")
            exit()

    print("Yes")
