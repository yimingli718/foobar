def answer(t, n):
    pre = [0] * n
    pre[0] = 1
    cur = [0] * n
    for step in range(t):
        pre = move(pre, cur, n)
        cur = [0] * n
    return pre[-1]



def move(pre, cur, n):
    for i in range(1, n-1):
        cur[i] = pre[i]
        cur[i] += (pre[i-1] + pre[i+1])
        cur[i] %= 123454321


    cur[0] = pre[0] + pre[1]
    cur[-2] -= pre[-1]
    cur[0] %= 123454321

    cur[-1] = pre[-1]
    cur[-1] += pre[-2]
    cur[-1] %= 123454321
    print cur
    return cur

print answer(5, 3)