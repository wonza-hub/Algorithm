ladder = []
a, b = 0, 0
for i in range(10):
    line = list(map(int, input().split()))
    for j in range(10):
        if i == 9:
            if line[j] == 2:
                a, b = i, j
    ladder.append(line)
check = [[0] * 10 for _ in range(10)]

dx = [0, 0, -1]
dy = [1, -1, 0]

def dfs(x, y):
    if x == 0:
        print(y)
        return
    else:
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < 10 and 0 <= ny < 10) and check[nx][ny] == 0:
                if ladder[nx][ny] == 1:
                    if i == 0 or i == 1:
                        check[nx][ny] = 1
                        dfs(nx, ny)
                        break
                    else:
                        check[nx][ny] = 1
                        dfs(nx, ny)
dfs(a, b)
                    
                    
            



                