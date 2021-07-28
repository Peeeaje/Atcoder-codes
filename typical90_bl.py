N, Q = map(int, input().split())
A = list(map(int, input().split()))
diff = [0 for i in range(len(A) - 1)]

for i in range(len(A)-1):
    diff[i] = A[i+1] - A[i]

ans = sum(map(abs, diff))
for i in range(Q):
    L, R, V = map(int, input().split())

    diff_abs = 0
    
    if L-2 != -1:
        diff_abs += abs(diff[L-2] + V) - abs(diff[L-2])
        diff[L-2] = diff[L-2] + V

    if R-1 != N-1:
        diff_abs += abs(diff[R-1] - V) - abs(diff[R-1])
        diff[R-1] = diff[R-1] - V

    ans += diff_abs
    print(ans)
   

