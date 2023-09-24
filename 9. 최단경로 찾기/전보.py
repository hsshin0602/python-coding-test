import heapq

INF = int(1e9)
n, m, c = map(int, input().split())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for i in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

hq = []
heapq.heappush(hq, (0, c))
distance[c] = 0

while hq:
    dist, node = heapq.heappop(hq)
    if distance[node] < dist:
        continue
    for i in graph[node]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(hq, (cost, i[0]))

cnt = 0
max_dist = 0
for i in distance:
    if i != INF:
        cnt += 1
        if max_dist < i:
            max_dist = i

print(cnt - 1, max_dist)
