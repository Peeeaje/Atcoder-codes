h, w, k = map(int, input().split())
S = [list(input()) for _ in range(h)]


ans = float('inf')
for i in range(h):
    s = S[i]

    # 尺取り法を用いる
    left = 0
    right = 0
    score = 0
    min_score = float('inf')

    while right < w:
        if right - left ==
        if s[right] == ".":
            score += 1
            right += 1
        elif s[right] == "o":
            right += 1
        else:
            left = right + 1
            right = left
            score = 0








