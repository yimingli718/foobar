def nCr(n,r):
    rst = 1
    if r == 0 or n == r:
        return rst
    r = min(r, n-r)
    for i in range(0, r):
        rst *= (n-i)
    for i in range(1, r+1):
	rst /= i
    return rst

class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class Tree:
    def __init__(self):
        self.root = None
		
    def add(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if(val < node.v):
            if(node.l != None):
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if(node.r != None):
                self._add(val, node.r)
            else:
                node.r = Node(val)

def possibleTree(tree):
    if tree.root != None:
        return _possibleTree(tree.root)

def _possibleTree(node):
    left = [0, 1]
    right = [0,1]
    if node.l:
        left = _possibleTree(node.l)
    if node.r:	
        right = _possibleTree(node.r)
    return [left[0]+right[0]+1, nCr(left[0]+right[0], left[0]) * left[1] * right[1]]

def answer(seq):
    bTree = Tree()
    for num in seq:
	bTree.add(num)
    return str(possibleTree(bTree)[1])

print answer([5, 9, 8, 2, 1])
print answer([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
