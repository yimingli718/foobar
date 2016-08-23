from itertools import combinations
from itertools import product

# Check valid solution available for odd sized matrix
# borrowed idea from http://math.stackexchange.com/a/441697/4471
def validAnswer(matrix):
    parities = -1
    for n in xrange(len(matrix)):
        if parities == -1:
	    parities = sum(matrix[n]) % 2
	if parities != sum(matrix[n]) % 2 or parities != sum([row[n] for row in matrix]) % 2:
	    return False
    return True

# Calculate even size matrix
def calcEven(matrix):
    n = len(matrix)
    rst = [[0 for c in xrange(n)] for r in xrange(n)]
    for r, c in product(range(n), repeat=2):
        if matrix[r][c]:
            rst[r] = [num ^ 1 for num in rst[r]]
            for row in rst:
                row[c] ^= 1
	    rst[r][c]  ^= 1
    return sum([sum([item for item in row]) for row in rst])
# Calculate odd size matrix with reducing to minimum
def calcOdd(matrix):
    n = len(matrix)
    rst = [[0 for x in xrange(n+1)] for y in xrange(n+1)]
    for r, c in product(range(n), repeat=2):
        if matrix[r][c]:
            rst[r] = [num ^ 1 for num in rst[r]]
            for row in rst:
                row[c] ^= 1
	    rst[r][c]  ^= 1
    # Reduced the solution to minimum
    mini = n**2
    parities = sum(matrix[0]) % 2
    for i in xrange(parities, n+1, 2):
        mini = min(mini, findMin(rst, i, parities))
    return mini

# Given number of lights flipped on the bottom row, find the minimum solution from 
# all the possible answers. 
def findMin(rst, numOf1s, parities):
    idxs = list(xrange(len(rst)-1))
    combos = [list(combo) for combo in combinations(idxs, numOf1s)]
    mini = len(rst) ** 2
    # Try all the possible combonations with same parities
    for combo in combos:
        newRst = [list(row) for row in rst] 
        for c in combo:
            for row in newRst:
                row[c] ^= 1
            newRst[-1] = [(d+1)%2 for d in newRst[-1]]
            newRst[-1][c] ^= 1
        for row in newRst[:-1]:
            row[-1] = sum(row[:-1])
        # Based on the sum of flipped lights on each row, find the minimum 
        newRst[0:-1] = sorted(newRst[0:-1], key=lambda x : x[-1], reverse = True)
        for r in xrange(parities, len(rst), 2):
            mini = min(mini, sum(len(rst)-1-row[-1] for row in newRst[:r]) + sum(row[-1] for row in newRst[r:-1]))
    return mini


def answer(matrix):
    if len(matrix)%2:
	if validAnswer(matrix):
            return calcOdd(matrix)
	else:
	    return -1
    else:
	return calcEven(matrix)


print answer([
    [0,0,1],
    [0,1,0],
    [1,0,0]
    ])

print answer([
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
])
