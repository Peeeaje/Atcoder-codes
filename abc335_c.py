n, q = map(int, input().split())
parts = [[i + 1, 0] for i in range(n)]

shift = 0

for _ in range(q):
    query = list(input().split())
    if query[0] == '1':
        dir = query[1]
        # リスト内の値をコピーして代入
        parts[-1 - shift] = parts[0 - shift].copy()  # 値のコピーを使用
        part = parts[-1 - shift]

        if dir == 'R':
            part[0] += 1
        elif dir == 'L':
            part[0] -= 1
        elif dir == 'U':
            part[1] += 1
        else:  # 'D'
            part[1] -= 1

        shift += 1
        shift %= n  # shiftがnを超えないようにモジュロ演算

    else:
        c = int(query[1])
        print(parts[c - 1 - shift][0], parts[c - 1 - shift][1])
