N = int(input())
A = list(map(int, input().split()))
ten_percent = sum(A) / 10
A = A + A

l, r = 0, 0
int_val = 0
while l < N:
    if int_val == ten_percent:
        print("Yes")
        exit()
    else:
        if int_val < ten_percent:
            r += 1
            int_val += A[r]
        else:
            l += 1
            int_val -= A[l]
print("No")
