from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

h, w = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h)]


def melt():
    ch = [[0] * w for _ in range(h)]
    q = deque([(0, 0)])
    ch[0][0] = 1
    melt_cnt = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and ch[nx][ny] == 0:
                ch[nx][ny] = 1
                # 공기와 맞닿은 치즈인 경우
                if arr[nx][ny] == 1:
                    arr[nx][ny] = 0
                    melt_cnt += 1
                # 공기인 경우
                else:
                    q.append((nx, ny))
    return melt_cnt


hour = 0
last = 0
while True:
    cnt = melt()
    if cnt == 0:
        print(hour)
        print(last)
        break
    last = cnt
    hour += 1