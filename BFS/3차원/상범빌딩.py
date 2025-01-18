from collections import deque

dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def solution(l, r, c):
    building = []
    q = deque()

    for _ in range(l):
        tmp = [list(input()) for _ in range(r)]
        building.append(tmp)
        input()

    for i in range(l):
        for j in range(r):
            for k in range(c):
                if building[i][j][k] == 'S':
                    building[i][j][k] = 0
                    q.append((i, j, k))

    while q:
        z, x, y = q.popleft()
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nz < l and 0 <= nx < r and 0 <= ny < c:
                if building[nz][nx][ny] == '.':
                    building[nz][nx][ny] = building[z][x][y] + 1
                    q.append((nz, nx, ny))
                if building[nz][nx][ny] == 'E':
                    print(f"Escaped in {building[z][x][y]+1} minute(s).")
                    return
    print('Trapped!')


while True:
    l, r, c = map(int, input().split())
    if l == 0 and r == 0 and c == 0:
        break
    solution(l, r, c)
