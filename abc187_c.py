import sys
import math

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readline

N = int(readline())
S = list(read().decode().split())
ex = set()
non_ex = set()
for s in S:
    if s[0] == "!":
        if s[1:] not in ex:
            ex.add(s[1:])
        if s[1:] in non_ex:
            print(s[1:])
            exit()

    else:
        if s not in non_ex:
            non_ex.add(s)
        if s in ex:
            print(s)
            exit()

print("satisfiable")
