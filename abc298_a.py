N = int(input())
S = set(input())

if 'o' in S and 'x' not in S:
    print('Yes')
else:
    print('No')