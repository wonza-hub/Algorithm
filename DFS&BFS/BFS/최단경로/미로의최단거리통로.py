from collections import deque

maze = [list(map(int, input().split())) for _ in range(7)]
q = deque([(0, 0, 0)])
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = 10e9

while q:
    x, y, now = q.popleft()
    if x == 6 and y == 6:
        ans = min(now, ans)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx and nx < 7 and 0 <= ny and ny < 7:
            if maze[nx][ny] == 0:
                maze[nx][ny] = now + 1
                q.append((nx, ny, now + 1))
if ans == 10e9:
    print(-1)
else:
    print(ans)