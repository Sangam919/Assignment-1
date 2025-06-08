from collections import OrderedDict

n = int(input())
words = [input().strip() for _ in range(n)]

counts = OrderedDict()
for word in words:
    counts[word] = counts.get(word, 0) + 1

print(len(counts))
print(*counts.values())
