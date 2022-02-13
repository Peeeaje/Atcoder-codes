import collections

N = int(input())
s = input()

if N == 1:
    print(s)
    exit()

alphabets = list("abcdefghijklmnopqrstuvwxyz")
s_list = list(s)
s_set = set(s_list)
c = collections.Counter(s_list)

used_alphabets = []
for left in alphabets:
    if left in s_set:
        used_alphabets.append(left)

index_deque = collections.defaultdict(collections.deque)
for left in range(N):
    string = s_list[left]
    index_deque[string].append(left)


right = N + 10
left = 0
x = []
popped = index_deque[used_alphabets[0]][-1]
for alphabet in used_alphabets:
    while len(index_deque[alphabet]) and left < right:
        # print(index_deque[alphabet])
        if s_list[left] == alphabet:
            index_deque[alphabet].popleft()
        else:
            popped = index_deque[alphabet].pop()
            if popped > right:
                pass
            else:
                right = popped
                if left < right:
                    x.append([left, right])
                    # print(left, right, popped)
        left += 1
        # print(alphabet, left)
# leftとrightを交換していく、leftは１ずつ増加、rightはa, b, cの順の中で遅いものから選ばれる
for a, b in x:
    s_list[a], s_list[b] = s_list[b], s_list[a]

print("".join(s_list))
