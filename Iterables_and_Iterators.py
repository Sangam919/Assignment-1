from itertools import combinations

n = int(input())
arr = input().split()
k = int(input())

total = list(combinations(arr, k))
count = 0
for c in total:
    if 'a' in c:
        count += 1

print(f"{count/len(total):.4f}")
