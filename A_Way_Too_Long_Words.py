cases = int(input())
for _ in range(cases):
    word = input()
    length = len(word)
    if length > 10:
        print(word[0] + str(len(word[1: length - 1])) + word[-1])
    else:
        print(word)
