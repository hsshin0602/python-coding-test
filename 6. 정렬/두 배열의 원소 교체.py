n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
print(sum(a))


# for _ in range(k):
#     min_a = a.index(min(a))
#     max_b = b.index(max(b))
#     temp = a[min_a]
#     a[min_a] = b[max_b]
#     b[max_b] = temp

# print(sum(a))
