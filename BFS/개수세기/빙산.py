from collections import deque
import sys
input=sys.stdin.readline

n, m = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(n)]
cnt = [[0] * m for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
year = 0


def count_sea_side(x, y):
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if ice[nx][ny] == 0:
            cnt += 1

    return cnt

def bfs(q,ch):
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if ice[nx][ny] and not ch[nx][ny]:
                ch[nx][ny]=1
                q.append((nx,ny))
    
def count_part():
    part=0
    q=deque()
    ch=[[0]*m for _ in range(n)]
    for i in range(1,n-1):
        for j in range(1,m-1):
            if ice[i][j]>0 and not ch[i][j]:
                part+=1
                # 조기 종료
                if part>1:
                    return part
                ch[i][j]=1
                q.append((i,j))
                bfs(q,ch)
    
    return part

while True:
    year += 1
    for i in range(1,n-1):
        for j in range(1,m-1):
            if ice[i][j] > 0:
                cnt[i][j] = count_sea_side(i, j)
    for i in range(1,n-1):
        for j in range(1,m-1):
            if ice[i][j] > 0:
                ice[i][j]=max(0,ice[i][j]-cnt[i][j])

    part=count_part()
    if part>1:
        print(year)
        break
    elif part==0:
        print(0)
        break
                