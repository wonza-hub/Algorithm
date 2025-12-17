import sys
input=sys.stdin.readline
from collections import deque

dx=[-1,0,1,0]
dy=[0,1,0,-1]

l,w=map(int,input().split())
arr=[list(input().rstrip()) for _ in range(l)]

def bfs(a,b):
    global ans
    ch=[[0]*w for _ in range(l)]
    ch[a][b]=1
    q=deque([(a,b,0)])
    while q:
        x,y,dis=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=l or ny<0 or ny>=w or ch[nx][ny]==1 or arr[nx][ny]=='W':
                continue
            ch[nx][ny]=1
            ans=max(ans,dis+1)
            q.append((nx,ny,dis+1))

ans=0
for i in range(l):
    for j in range(w):
        # 모든 육지를 시작점으로 두고 bfs 수행
        if arr[i][j]=='W':
            continue
        bfs(i,j)
print(ans)