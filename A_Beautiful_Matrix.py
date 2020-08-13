for j in range(5):
    row = [int(x) for x in input().split(" ")]
    if 1 in row:
        i = row.index(1)
        if j >= 2:
            j -= 2
        else:
            j = 2 - j
        if i >= 2:
            i -= 2
        else:
            i = 2 - i
        print(j + i)
