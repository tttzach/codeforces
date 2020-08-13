problems = int(input())
result = 0
for _ in range(problems):
    line = [int(x) for x in input().split(" ")]
    if line.count(1) >= 2:
        result += 1
print(result)
