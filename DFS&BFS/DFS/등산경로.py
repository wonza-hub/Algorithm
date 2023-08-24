n = int(input())
dep = 10e9
arr = -10e9
a, b = -1, -1
cnt = 0
mount = []
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] < dep:
            dep = line[j]
            a, b = i, j
        elif line[j] > arr:
            arr = line[j]
    mount.append(line)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    global cnt
    if mount[x][y] == arr:
        cnt += 1
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if mount[nx][ny] > mount[x][y]:
                    dfs(nx, ny)


dfs(a, b)
print(cnt)
