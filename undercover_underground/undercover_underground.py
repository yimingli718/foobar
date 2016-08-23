from math import pow

def nCr(n, r):
    rst = 1;
    if r == 0:
        return rst;
    for i in range(0, r):
        rst *= (n-i)
    for i in range(0, r):
        rst /= i+1
    return rst

def answer(N, K):
    if K < N-1:
        return nCr(nCr(N,2), K)
    if K > nCr(N-1, 2):
        #If num of edges of N is greater than N-1, then there is isolate vertex
        return nCr(nCr(N,2), K)
    else:
        #could be one or more isolated vertex
        total = nCr(nCr(N,2), K)
        for i in range(1, N):
            for e in range(i-1, min(nCr(i,2)+1, K)+1):
                if K-e <= nCr(N-i, 2):
                    total -= nCr(N-1, i-1) * answer(i,e) * nCr(nCr(N-i, 2), K-e)
        return total

