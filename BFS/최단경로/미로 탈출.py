from collections import deque

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def bfs(sx,sy,ex,ey):
    mark=[[0 for _ in range(m)] for _ in range(n)]
    ch=[[0 for _ in range(m)] for _ in range(n)]
    min_d=0
    q=deque()
    q.append((sx,sy))
    ch[sx][sy]=1
    while q:
        x,y=q.popleft()
        if x==ex and y==ey:
            return mark[x][y]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and nmaps[nx][ny]!='X' and ch[nx][ny]==0:
                mark[nx][ny]=mark[x][y]+1
                ch[nx][ny]=1
                q.append((nx,ny))
    
def solution(maps):
    answer = 0
    global nmaps
    nmaps=[list(m) for m in maps]
    global n,m
    n,m=len(nmaps),len(nmaps[0])
    sx,sy,ex,ey,lx,ly=-1,-1,-1,-1,-1,-1
    for i in range(n):
        for j in range(m):
            if nmaps[i][j]=='S':
                sx,sy=i,j
            if nmaps[i][j]=='E':
                ex,ey=i,j
            if nmaps[i][j]=='L':
                lx,ly=i,j
    a=bfs(sx,sy,lx,ly)
    if a==None:
        return -1
    b=bfs(lx,ly,ex,ey)
    if b==None:
        return -1
    
    return a+b