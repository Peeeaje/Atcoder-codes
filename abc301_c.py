from collections import Counter

s = list(input())
t = list(input())

s_counter = Counter(s)
t_counter = Counter(t)

l, r = 0, 0
for v in 'abcdefghijklmnopqrstuvwxyz':
    min_ = min(s_counter[v], t_counter[v])
    s_counter[v] -= min_
    t_counter[v] -= min_

    if v not in set('atcoder') and (s_counter[v] > 0 or t_counter[v] > 0):
        print('No')
        exit()

    l += s_counter[v]
    r += t_counter[v]

if l + r <= s_counter['@'] + t_counter['@']:
    print('Yes')
else:
    print('No')
