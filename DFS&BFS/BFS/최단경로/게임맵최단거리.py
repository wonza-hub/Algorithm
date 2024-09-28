#게임 맵의 상태 maps
#maps는 0과 1로만 이루어져 있으며, 0은 벽이 있는 자리, 1은 벽이 없는 자리를 나타냅니다.
#캐릭터가 상대 팀 진영에 도착하기 위해서 지나가야 하는 칸의 개수의 최솟값
#
#단, 상대 팀 진영에 도착할 수 없을 때는 -1을 return

from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
def solution(maps):
    n, m = len(maps), len(maps[0])
    q = deque()
    x, y = 0, 0
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]            
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx, ny))
                
    return -1 if maps[n - 1][m - 1] == 1 else maps[n - 1][m - 1]