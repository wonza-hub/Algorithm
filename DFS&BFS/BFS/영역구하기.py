import sys
input = sys.stdin.readline
from collections import deque

m, n, k = map(int, input().split())
grid = [[0] * m for _ in range(n)]

def draw_rectangle(sx, sy, ex, ey):
    for x in range(sx, ex):
        for y in range(sy, ey):
            grid[x][y] = 1

for _ in range(k):
    sa, sb, ea, eb = map(int, input().split())
    draw_rectangle(sa, sb, ea, eb)

cnt = 0
area_list = []
q = deque()

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            cnt += 1
            grid[i][j] = 1
            area = 1
            q.append((i, j))
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < m:
                        if grid[nx][ny] == 0:
                            grid[nx][ny] = 1
                            area += 1
                            q.append((nx, ny))
            area_list.append(area)
print(cnt)
print(' '.join(map(str, sorted(area_list))))
                            
