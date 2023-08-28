# BFS
from collections import deque

n, m = map(int, input().split())
graph = [
    [1, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

stack = deque()
stack.append((0, 0))
while stack:
    x, y = stack.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y] + 1
            stack.append((nx, ny))

print(graph[n - 1][m - 1])
