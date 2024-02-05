from collections import deque

graph = []
ans = int(1e9)

n, m = map(int, input().split())
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

q = deque([(0, 0, 1)])

while q:
    x, y, now = q.popleft()
    if x == n - 1 and y == m - 1:
        ans = min(ans, now)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny, now + 1))

print(ans)