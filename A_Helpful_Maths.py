import heapq

array = input().split("+")
heapq.heapify(array)
result = []

for _ in range(len(array)):
    result.append(heapq.heappop(array))

print("+".join(result))
