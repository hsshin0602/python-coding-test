import sys

N, M, K = map(int, sys.stdin.readline().split())
arr = list(map(int, input().split()))

arr.sort()
first = arr[-1]
second = arr[-2]

result = 0
count = 0
for _ in range(M):
    if count != K:
        result += first
        count += 1
    else:
        count = 0
        result += second
print(result)
