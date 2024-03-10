import sys
sys.setrecursionlimit(100000)

n = int(input())
graph = []
max_h = 0
min_h = 101
ans = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(n):
    tmp = list(map(int, input().split()))
    max_h = max(max_h, max(tmp))
    min_h = min(min_h, min(tmp))
    graph.append(tmp)


def dfs(x, y, h):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] > h and ch[nx][ny] == 0:
                ch[nx][ny] = 1
                dfs(nx, ny, h)

for height in range(min_h - 1, max_h + 1):
    ch = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > height and ch[i][j] == 0:
                cnt += 1
                dfs(i, j, height)
    ans = max(ans, cnt)
    
print(ans)