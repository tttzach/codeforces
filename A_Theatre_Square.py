import math

n, m, a = [int(x) for x in input().split(" ")]

numTileHorizontal = math.ceil(m/a)
numTileVertical = math.ceil(n/a)
print(numTileHorizontal * numTileVertical)
