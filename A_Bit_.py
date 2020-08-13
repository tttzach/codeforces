x = 0

numOperations = int(input())

for _ in range(numOperations):
    operation = input()
    if operation == "X++" or operation == "++X":
        x += 1
    elif operation == "X--" or operation == "--X":
        x -= 1

print(x)
