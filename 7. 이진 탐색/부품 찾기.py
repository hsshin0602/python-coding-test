import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, input().split()))
m = int(sys.stdin.readline().rstrip())
arr1 = list(map(int, input().split()))


def binary_search(lst, start, end, target):
    mid = (start + end) // 2
    if start > end:
        return

    if lst[mid] == target:
        return mid
    elif lst[mid] > target:
        binary_search(lst, start, mid - 1, target)
    else:
        binary_search(lst, mid + 1, end, target)


arr.sort()
for i in arr1:
    check = binary_search(arr, 0, n - 1, i)
    if check:
        print("yes", end=" ")
    else:
        print("no", end=" ")
