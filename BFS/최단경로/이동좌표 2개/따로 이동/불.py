from collections import deque

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def solution():
    while q:
        x,y,who=q.popleft()
        if who=='@' and (x==0 or x==h-1 or y==0 or y==w-1):
            return res[x][y]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<h and 0<=ny<w:
                if who=='*' and (arr[nx][ny]!='#' and arr[nx][ny]!='*'):
                    arr[nx][ny]='*'
                    q.append((nx,ny,'*'))
                if who=='@' and arr[nx][ny]=='.' and not res[nx][ny]:
                    res[nx][ny]=res[x][y]+1
                    q.append((nx,ny,'@'))

    return -1

for _ in range(int(input())):
    w,h=map(int,input().split())
    q=deque()
    life=0
    arr=[list(input()) for _ in range(h)]
    res=[[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if arr[i][j]=='*':
                q.appendleft((i,j,'*'))
            if arr[i][j]=='@':
                q.append((i,j,'@'))
                res[i][j]=1

    ans=solution()
    if ans==-1:
        print('IMPOSSIBLE')
    else:
        print(ans)