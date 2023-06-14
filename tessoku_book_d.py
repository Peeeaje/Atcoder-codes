N = int(input())

N = bin(N)[2:]
n = len(N)

print("0" * (10 - n) + N)
