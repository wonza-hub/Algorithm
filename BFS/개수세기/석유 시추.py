from collections import deque

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def cnt(a,b,land,arr):
    global m,n
    global ch
    s=set()
    count=0
    q=deque([])
    q.append((a,b))
    s.add(b)
    ch[a][b]=1
    count+=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and land[nx][ny]==1 and not ch[nx][ny]:
                ch[nx][ny]=1
                s.add(ny)
                count+=1
                q.append((nx,ny))
    for col in s:
        arr[col]+=count

    return count
    
def solution(land):
    answer = 0
    # m:가로,n:세로
    global m,n
    m,n=len(land[0]),len(land)
    global ch
    ch=[[0]*m for _ in range(n)]
    arr=[0]*m
    for i in range(n):
        for j in range(m):
            if ch[i][j]:
                continue
            
            if land[i][j]==1:
                count=cnt(i,j,land,arr)
        
    return max(arr)