d = {}

def find(index):
    if index not in d:
        n = int(index/2)
        if index % 2 == 1:
            d[index] = find(n) + find(n-1) + 1
        else:
            d[index] = find(n) + find(n+1) + n
    return d[index]

def bSearch(first, last, target, odd):
    #mid = first + ((last - first) >> 1)
    #mid += odd != mid & 1
    if first >= last:
        return -1
    mid = (first + last)/2
    if mid & 1 != odd:
        mid += 1
    rst = find(mid)
    if rst  == target:
        return mid
    elif rst < target:
        return bSearch(mid+1, last, target, odd)
    else:
        return bSearch(first, mid-1, target, odd)
        
def answer(str_S):
    target = int(str_S)
    d.update({0:1, 1:1, 2:2, 3:3, 5:4, 7:6})
    if target <= 2:
        return str(d[target])
    odd = bSearch(0, target+1, target, 1)
    even = bSearch(0, target+1, target, 0)
    if odd >= 0 or even >= 0:
        if odd > even:
            return str(odd)
        else:
            return str(even)
    else:
        return "None"
