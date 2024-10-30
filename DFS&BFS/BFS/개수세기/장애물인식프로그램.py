from collections import deque
import sys
input=sys.stdin.readline

dx=[-1,0,1,0]
dy=[0,1,0,-1]

n=int(input())
graph=[list(map(int,list(input().rstrip()))) for i in range(n)]

ans=[]
blk=0

def bfs(i,j):
    cnt=1
    q=deque()
    q.append((i,j))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]==1:
                cnt+=1
                q.append((nx,ny))
                graph[nx][ny]=0
    return cnt

for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            blk+=1
            graph[i][j]=0
            cnt=bfs(i,j)
            ans.append(cnt)
        
ans.sort()
print(blk)
for a in ans:
    print(a)
            