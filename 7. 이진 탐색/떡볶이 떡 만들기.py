n, m = map(int, input().split())
lst = list(map(int, input().split()))


def binary_search(lst, start, end, target):
    # 떡 길이의 중간값
    result = 0
    while start <= end:
        mid = (start + end) // 2
        sum = 0
        for i in range(n):
            dis = lst[i] - mid
            if dis > 0:
                sum += dis

        if sum == target:
            return mid
        elif sum > target:
            start = mid + 1
            result = mid
        else:
            end = mid - 1
    return result


print(binary_search(lst, 0, max(lst), m))
