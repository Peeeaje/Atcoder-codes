H, W, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if sum(A) % K != sum(B) % K:
    print(-1)
    exit()


