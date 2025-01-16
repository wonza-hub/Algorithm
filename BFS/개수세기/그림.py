from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n, m = map(int, input().split())
picture = [list(map(int, input().split())) for _ in range(n)]
ch = [[0] * m for _ in range(n)]
q = deque()
cnt, max_area = 0, 0


def bfs(i, j, area):
    q.append((i, j))
    picture[i][j] = 0
    area += 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and picture[nx][ny]:
                picture[nx][ny] = 0
                area += 1
                q.append((nx, ny))

    return area


for i in range(n):
    for j in range(m):
        if picture[i][j]:
            cnt += 1
            area = 0
            area = bfs(i, j, area)
            max_area = max(max_area, area)
print(cnt)
print(max_area)
