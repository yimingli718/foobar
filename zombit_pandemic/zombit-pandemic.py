from math import factorial

graphCache = {}
cache = []

def nCr(n, r):
    if r == 0 or n == r:
        return 1
    r = min(r, (n-r))
    rst = 1
    for i in range(0, r):
        rst *= (n - i)
    for i in range(1, r+1):
        rst /= i
    return rst

# n vertices, n vertices directed graph
# a(n) = sum(k=1, n-1, binomial(n, k)*(n-k)^(n-k)*k^k) / n
# n >= 2
def dGraph(n):
    if n not in graphCache:
        graphCache[n] = sum([nCr(n, k) * ((n-k)**(n-k)) * (k ** k) for k in range(1, n)]) / n
    return graphCache[n]

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def preBuild(n):
    if n < len(cache):
        return None
    
    for totalVerNum in range(len(cache), n+1):
        cache.append([])
        # verNum is the connected directed graph with most vectices
        # all the other connected directed graph will have either equal or less number of vertices
        for verNum in range(0, totalVerNum+1):
            cache[totalVerNum].append(0)
            if verNum > 1:
                # g is number of graph with VerNum vertices
                for gNum in range(1, totalVerNum/verNum+1):
                    # l vertices left
                    l = totalVerNum - gNum * verNum
                    # total is num of different forest
                    total = nCr(totalVerNum, gNum*verNum)
                    # each graph with verNum vertices has dGraph(verNum) ways to organize
                    for g in range(0, gNum):
                        total *= nCr((gNum-g)*verNum, verNum)
                        total *= dGraph(verNum)
                    total /= factorial(gNum)
                    if l != 0:
                        total *= sum(cache[l][0:verNum])
                    cache[totalVerNum][verNum] += total

def answer(n):
    preBuild(n)
    num = 0
    for i in range(0, len(cache[n])):
        num += (i * cache[n][i])    
    denom = (n-1)**n
    d = max(1, gcd(num, denom))
    return str(num/d) + "/" + str(denom/d)

for i in range(0, 51):
    print answer(i)

for lst in cache:
    print lst