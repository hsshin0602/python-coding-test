n = int(input())

arr = []
for _ in range(n):
    data = input().split()
    arr.append((data[0], data[1]))

result = sorted(arr, key=lambda x: x[1])
print(result)
