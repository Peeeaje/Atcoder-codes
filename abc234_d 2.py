import heapq

N, K = map(int, input().split())
P = list(map(int, input().split()))
# 新しく入った数値が、前の出力よりも大きいなら、答えは更新される
# 新しく入った数値が、前の出力よりも小さいなら、答えは更新されない
# popleft()と新しく入った数値で、小さい方を答えとして更新する
que = P[:K]
heapq.heapify(que)
x = heapq.heappop(que)
print(x)

for i in range(K, N):
    if P[i] > x:
        heapq.heappush(que, P[i])
        x = heapq.heappop(que)
        print(x)
    else:
        print(x)
