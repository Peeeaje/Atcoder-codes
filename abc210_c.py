N, K = map(int, input().split())
c = list(map(int, input().split()))
ans = -1
import collections

temp = collections.deque(c[:K], K)
c = c[K:]
c = collections.deque(c)
ans = len(list(set(temp)))

for i in range(N - K):
    temp.append(c.popleft())
    ans = max(ans, len(list(set(temp))))

print(ans)
