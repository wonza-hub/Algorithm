from collections import deque

m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
queue = deque([])
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
res = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            queue.append([i, j])

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append([nx, ny])

bfs()
for i in matrix:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))
print(res - 1)

# 복습 풀이
from collections import deque

m,n=map(int,input().split())
tomatoes=[list(map(int,input().split())) for _ in range(n)]

dx=[-1,0,1,0]
dy=[0,1,0,-1]
ans=0
empty_cnt=0

q=deque()
for i in range(n):
    for j in range(m):
        if tomatoes[i][j]==1:
            q.append((i,j))
        elif tomatoes[i][j]==0:
            empty_cnt+=1

def bfs():
    global ans,empty_cnt
    if empty_cnt==0:
        return
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and tomatoes[nx][ny]==0:
                empty_cnt-=1
                tomatoes[nx][ny]=tomatoes[x][y]+1
                ans=max(ans,tomatoes[nx][ny]-1)
                q.append((nx,ny))
    if empty_cnt:
        ans=-1

bfs()
print(ans)