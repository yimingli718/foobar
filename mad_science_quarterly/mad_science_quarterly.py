def answer(L, k):
    sums = []
    head = end = 0
    cSum = mSum = 0
    while head <len(L) and end <= len(L):
        if end == len(L):
            cSum -= L[head]
            head += 1
        elif cSum >= 0:
            if end - head < k and end >= head:
                cSum += L[end]
                end += 1
            else:
                cSum -= L[head]
                head += 1
        else:
            if end >= head:
                cSum -= L[head]
                head += 1
        mSum = max(mSum, cSum)
    return mSum

print answer([3,4,-8, 9, 10], 3)
