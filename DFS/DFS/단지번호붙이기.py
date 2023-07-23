n = int(input())
estate = [list(map(int, input())) for _ in range(n)]
list = []

dx = [-1, 0 ,1, 0]
dy = [0, 1 ,0, -1]

def dfs(x, y):
    global house_cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if estate[nx][ny] == 1:
                estate[nx][ny] = -1
                dfs(nx, ny)
                house_cnt += 1
                
for i in range(n):
    for j in range(n):
        if estate[i][j] == 1:
            house_cnt = 1
            estate[i][j] = -1
            dfs(i, j)
            list.append(house_cnt)

print(len(list))
list.sort()
for house_cnt in list:
    print(house_cnt)
    