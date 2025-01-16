import sys
sys.setrecursionlimit(10**6)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, maps, food):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if ch[nx][ny] or maps[nx][ny] == 'X':
                continue
            ch[nx][ny] = 1
            food += int(maps[nx][ny])
            food = dfs(nx, ny, maps, food)
    return food
        
def solution(maps):
    answer = []
    global m, n
    m = len(maps)
    n = len(maps[0])
    global ch
    ch = [[0] * n for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            if maps[i][j] != 'X' and not ch[i][j]:
                ch[i][j] = 1
                food = int(maps[i][j])
                food = dfs(i, j, maps, food)
                answer.append(food)
    
    return sorted(answer) if answer else [-1]
