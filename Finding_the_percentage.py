n = int(input())
data = {}
for _ in range(n):
    line = input().split()
    data[line[0]] = list(map(float, line[1:]))

name = input()
scores = data[name]
average = sum(scores) / len(scores)
print(format(average, ".2f"))
