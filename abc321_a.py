n = input()


for i in range(1, len(n)):
    if n[i - 1] > n[i]:
        continue
    print("No")
    exit()

print("Yes")