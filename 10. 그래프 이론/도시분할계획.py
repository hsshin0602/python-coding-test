n, m = map(int, input().split())
parent = [0] * (n + 1)
edges = []
result = 0

for i in range(1, n + 1):
    parent[i] = i

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()


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


for edge in edges:
    cost, a, b = edge
    if parent_find(parent, a) != parent_find(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost

print(result - last)
