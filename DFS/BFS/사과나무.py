from collections import deque

n = int(input())
farm = [list(map(int, input().split())) for _ in range(n)]
check = [[0] * n for _ in range(n)]
sum = 0
sum += farm[n//2][n//2]
check[n//2][n//2] = 1

q = deque([(n//2, n//2)])
l = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while q:
    if l == n//2:
        break
    for _ in range(len(q)):
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if check[nx][ny] == 0:
                q.append((nx, ny))
                sum += farm[nx][ny]
                check[nx][ny] = 1
    l += 1

print(sum)