import math
import itertools

def findLine(point0, point1):
    if point0[1] == point1[0]:
        return None
    a = float(point1[1] - point0[1])/(point1[0] - point0[0])
    b = point0[1] - a * point0[0]
    return [a, b]

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
    
def calc(p1, p2):
    deltaX = p1[0] - p2[0]
    deltaX = -deltaX if deltaX < 0 else deltaX
    deltaY = p1[1] - p2[1]
    deltaY = -deltaY if deltaY < 0 else deltaY
    extra = gcd(deltaX, deltaY) + 1
    return (extra + (deltaX + 1)*(deltaY + 1)) / 2 - 1

def answer(vertices):
    verticesX = sorted(vertices, key = lambda point : point[0])
    verticesY = sorted(vertices, key = lambda point : point[1])
    total = (1 + verticesX[2][0] - verticesX[0][0]) * (1 + verticesY[2][1] - verticesY[0][1])
    for x in range(0,2):
        for y in range(x+1, 3):
            total -= calc(vertices[x], vertices[y])

    if verticesX[1] == verticesY[1]:
        diagnol = findLine(verticesX[0], verticesX[2])
        if verticesX[1][1] <= verticesX[1][0] * diagnol[0] + diagnol[1]:
            if(diagnol[1] > 0):
                total -= (verticesX[2][0] - verticesX[1][0]) * (verticesX[1][1] - verticesY[0][1])
            else:
                total -= (verticesX[1][0] - verticesX[0][0]) * (verticesX[1][1] - verticesY[0][1])
        else:
            if(diagnol[1] > 0):
                total -= (verticesX[1][0] - verticesX[0][0]) * (verticesX[2][1] - verticesY[1][1])
            else:
                total -= (verticesX[2][0] - verticesX[1][0]) * (verticesX[2][1] - verticesY[1][1])
    return total

print(answer([[91207, 89566], [-88690, -83026], [67100, 47194]]))
