from collections import deque

n = int(input())
islands = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

q = deque()

dx = [-1, -1, 0, 1, 1, 1, 0 ,-1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for i in range(n):
    for j in range(n):
        if islands[i][j] == 1:
            cnt += 1
            islands[i][j] = 0
            q.append((i, j))
            while q:
                x, y = q.popleft()
                for k in range(8):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if islands[nx][ny] == 1:
                            islands[nx][ny] = 0
                            q.append((nx, ny))

print(cnt)


                