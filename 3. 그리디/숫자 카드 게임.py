N, M = map(int, input().split())

result = 0
for _ in range(N):
    arr = list(map(int, input().split()))
    min_num = min(arr)
    result = max(result, min_num)
print(result)
