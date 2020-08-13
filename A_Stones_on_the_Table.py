n = int(input())
stones = [char for char in input()]
length = len(stones)
min = 0
fast = 1
slow = 0

while fast < length and slow < length:
    if stones[slow] != stones[fast]:
        slow = fast
        fast += 1
    else:
        fast += 1
        min += 1

print(min)
