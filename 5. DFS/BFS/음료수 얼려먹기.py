from collections import deque

n, m = map(int, input().split())
graph = [[0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]

visit = [[0] * m for _ in range(n)]
queue = deque()
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
cnt = 0


def bfs(i, j):
    queue.append([i, j])

    while queue:
        x, y = queue.popleft()
        visit[x][y] = 1
        # 상하좌우 확인
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if visit[nx][ny] == 0 and graph[nx][ny] == 0:
                    queue.append([nx, ny])


for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and visit[i][j] == 0:
            bfs(i, j)
            cnt += 1
print(cnt)
