import sys
input=sys.stdin.readline
from collections import deque

n=int(input().rstrip())
arr=[list(input().rstrip()) for _ in range(n)]
INF=int(1e9)
cnt=[[INF]*n for _ in range(n)]
cnt[0][0]=0

q=deque()
q.append((0,0))
dx=[-1,0,1,0]
dy=[0,1,0,-1]

while q:
    x,y=q.popleft()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        # 다익스트라 개념과 같이, 방문했던 곳을 계속 방문하여 최솟값을 계속 갱신해야 함
        if 0<=nx<n and 0<=ny<n:
            if arr[nx][ny]=='1' and cnt[nx][ny]>cnt[x][y]:
                cnt[nx][ny]=cnt[x][y]
                q.append((nx,ny))
            elif arr[nx][ny]=='0' and cnt[nx][ny]>cnt[x][y]:
                cnt[nx][ny]=cnt[x][y]+1
                q.append((nx,ny))

print(cnt[n-1][n-1])