k, g, m = map(int, input().split())

g_amount, m_amount = 0, 0
for i in range(k):
    if g_amount == g:
        g_amount = 0

    elif m_amount == 0:
        m_amount = m

    else:
        trans = min(g - g_amount, m_amount)
        g_amount += trans
        m_amount -= trans

print(g_amount, m_amount)