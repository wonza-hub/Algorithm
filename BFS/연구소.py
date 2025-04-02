# python3 불통 / pypy 통
from collections import deque
import copy
import sys
input=sys.stdin.readline

dx=[-1,0,1,0]
dy=[0,1,0,-1]

n,m=map(int,input().rstrip().split())
arr=list(list(map(int,input().rstrip().split())) for _ in range(n))
ans=0

q=deque()
for i in range(n):
    for j in range(m):
        if arr[i][j]==2:
            q.append((i,j))

# 빈 공간을 세는 함수
def count_0(arr):
    global ans,n
    cnt=0
    for i in range(n):
        cnt+=arr[i].count(0)
    ans=max(ans,cnt)

# 바이러스를 퍼뜨리는 함수
def bfs(): 
    tmp_arr=copy.deepcopy(arr)
    vq=q.copy()
    
    while vq:
        x,y=vq.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and tmp_arr[nx][ny]==0:
                tmp_arr[nx][ny]=2
                vq.append((nx,ny))
    count_0(tmp_arr)

def wall(l):
    if l==3: # 벽이 3개가 되면 바이러스 퍼뜨리기
        bfs()
        return
    
    for i in range(n):
        for j in range(m):
            if arr[i][j]==0: # 빈 공간이어야 벽 세우기 가능
                arr[i][j]=1
                wall(l+1)
                arr[i][j]=0

wall(0)
print(ans)
