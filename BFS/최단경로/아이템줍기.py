from collections import deque 

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    graph = [[-1] * 102 for _ in range(102)]
    
    for rec in rectangle:
        x1, y1, x2, y2 = map(lambda x: x * 2, rec)
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    graph[i][j] = 0
                elif graph[i][j] != 0:
                    graph[i][j] = 1
    
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    q = deque()
    q.append([characterX * 2, characterY * 2])
    ch = [[-1] * 102 for _ in range(102)]
    ch[characterX * 2][characterY * 2] = 0
    
    while q:
        x, y = q.popleft()
        if x == itemX * 2 and y == itemY * 2:
            answer = ch[x][y] // 2
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if graph[nx][ny] == 1 and ch[nx][ny] == -1:
                ch[nx][ny] = ch[x][y] + 1
                q.append([nx, ny])
    
    return answer