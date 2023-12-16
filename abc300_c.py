H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]


def is_central(i, j):
    if i < 1 or i >= H - 1:
        return False
    if j < 1 or j >= W - 1:
        return False

    if C[i][j] == '.':
        return False
    if C[i - 1][j - 1] == '.':
        return False
    if C[i - 1][j + 1] == '.':
        return False
    if C[i + 1][j - 1] == '.':
        return False
    if C[i + 1][j + 1] == '.':
        return False
    return True


def check_corners(i, j, n):
    a = C[i + n][j + n] if i + n < H and j + n < W else '.'
    b = C[i - n][j - n] if i - n >= 0 and j - n >= 0 else '.'
    c = C[i + n][j - n] if i + n < H and j - n >= 0 else '.'
    d = C[i - n][j + n] if i - n >= 0 and j + n < W else '.'
    return any([a == '#', b == '#', c == '#', d == '#'])


def get_size(i, j):
    if not is_central(i, j):
        return 0

    size = 1
    for n in range(2, min(H, W) + 1):
        if not check_corners(i, j, n):
            break
        size += 1
    return size


ans = [0] * min(H, W)
for i in range(H):
    for j in range(W):
        if is_central(i, j):
            size = get_size(i, j)
            ans[size - 1] += 1
print(*ans)