import sys
input=sys.stdin.readline
from collections import deque

dx=[-1,0,1,0]
dy=[0,1,0,-1]

n,m,k=map(int,input().split())
arr=[[0]*(m+1) for _ in range(n+1)]
for _ in range(k):
    r,c=map(int,input().split())
    arr[r][c]=1

def bfs(a,b):
    q=deque()
    q.append((a,b))
    arr[a][b] = 0
    cnt=0

    while q:
        x,y=q.popleft()
        cnt+=1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<nx<=n and 0<ny<=m and arr[nx][ny]==1:
                arr[nx][ny]=0
                q.append((nx,ny))
    return cnt

ans=1
for i in range(1,n+1):
    for j in range(1,m+1):
        if arr[i][j]==1:
            cnt=bfs(i,j)
            ans=max(ans,cnt)
print(ans)


