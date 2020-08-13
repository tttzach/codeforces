m, n = [int(x) for x in input().split(" ")]

placed = 0

if m >= 2 and n >= 1:
    placeVertically = m // 2 * n
    verticalRemainder = m % 2
    if verticalRemainder:
        placeVertically += n // 2
    placed = placeVertically
elif m >= 1 and n >= 2:
    placeHorizontally = n // 2 * m
    horizontalRemainder = n % 2
    if horizontalRemainder:
        placeHorizontally += m // 2
    placed = placeHorizontally

print(placed)
