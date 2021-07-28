import sys
import numpy as np
import math

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


A, B = map(int, input().split())

lcm_ans = A * B // math.gcd(A, B)
print("Large" if lcm_ans > 10 ** 18 else lcm_ans)
