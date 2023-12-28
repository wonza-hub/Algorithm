import sys
input = sys.stdin.readline
from collections import deque

countries = []
n, l, r = map(int,input().split())
for _ in range(n):
    countries.append(list(map(int,input().split())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def bfs(a,b):
    q = deque()
    union = []
    q.append((a,b))
    union.append((a,b))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if l <= abs(countries[nx][ny] - countries[x][y]) <= r:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                    union.append((nx,ny))
    return union

ans = 0
while 1:
    visited = [[0] * (n+1) for _ in range(n+1)]
    flag = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                country = bfs(i,j)
                if len(country) > 1:
                    flag = 1
                    number = sum([countries[x][y] for x, y in country]) // len(country)
                    for x,y in country:
                        countries[x][y] = number
    if flag == 0:
        break
    ans += 1
print(ans)