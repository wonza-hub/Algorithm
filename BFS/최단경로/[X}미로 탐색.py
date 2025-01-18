# 파라미터로 넘기는 방법
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

# 직접 기록하는 방법
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
maze = []
for _ in range(n):
    tmp = list(map(int, input()))
    tmp = [-1 if ele == 1 else ele for ele in tmp]
    maze.append(tmp)

q = deque()
q.append((0, 0))
maze[0][0] = 1
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == -1:
            maze[nx][ny] = maze[x][y] + 1
            q.append((nx, ny))

print(maze[n - 1][m - 1])
