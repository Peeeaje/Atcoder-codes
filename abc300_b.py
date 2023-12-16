h, w = map(int, input().split())
A = [list(input()) for _ in range(h)]
B = [list(input()) for _ in range(h)]


def func1(A):
    return A[1:] + [A[0]]

def func2(A):
    return [a[1:] + [a[0]] for a in A]

C = A
for i in range(h):
    C = func1(C)
    for j in range(w):
        C = func2(C)

        if C == B:
            print('Yes')
            exit()
print('No')