n, m = map(int, input().split())


def parent_find(parent, x):
    if parent[x] != x:
        parent[x] = parent_find(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = parent_find(parent, a)
    b = parent_find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


parent = [0] * (n + 1)

for i in range(n + 1):
    parent[i] = i

for i in range(m):
    k, a, b = map(int, input().split())
    if k == 0:
        union_parent(parent, a, b)
    else:
        if parent[a] != parent[b]:
            print("NO")
        else:
            print("YES")
