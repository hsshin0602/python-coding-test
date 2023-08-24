N, M = map(int, input().split())
A, B, d = map(int, input().split())
graph = []
for _ in range(N):
    inp = list(map(int, input().split()))
    graph.append(inp)

visit = [[0] * M for _ in range(N)]

visit[A][B] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

dictect = d
count = 1
turn_cnt = 0
while True:
    dictect -= 1
    if dictect < 0:
        dictect = 3

    nx, ny = A + dx[dictect], B + dy[dictect]
    if visit[nx][ny] == 0 and graph[nx][ny] == 0:
        count += 1
        visit[nx][ny] = 1
        A, B = nx, ny
        turn_cnt = 0
        continue
    else:
        turn_cnt += 1

    if turn_cnt == 4:
        nx, ny = A - dx[dictect], B - dy[dictect]
        if graph[nx][ny] == 0:
            A, B = nx, ny
        else:
            break
        turn_cnt = 0
