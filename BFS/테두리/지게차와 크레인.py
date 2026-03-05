from collections import defaultdict,deque

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def bfs(x,y,arr,m,n,con,ch):
    global dic,cnt
    ch[0][0]=1
    q=deque([(0,0)])
    
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or n<=nx or ny<0 or m<=ny:
                continue
            if ch[nx][ny]:
                continue
            ch[nx][ny]=1
            # 지게차가 접근 가능
            if arr[nx][ny]==con:
                dic[arr[nx][ny]]-=1
                cnt-=1
                arr[nx][ny]=0
            # 키 포인트
            elif arr[nx][ny]==0:
                q.append((nx,ny))
        
        
def 지게차(arr,con,m,n):
    ch=[[0]*m for _ in range(n)]
    bfs(0,0,arr,m,n,con,ch)
    
def 크레인(arr,con,m,n):
    global dic,cnt
    for i in range(n):
        for j in range(m):
            if arr[i][j]==con:
                dic[arr[i][j]]-=1
                cnt-=1
                arr[i][j]=0
    
def solution(storage, requests):
    global dic,cnt
    dic=defaultdict(int)
    answer = 0
    arr=[[0]*(len(storage[0])+2)]
    
    for s in storage:
        arr.append([0]+list(s)+[0])
    arr.append([0]*(len(storage[0])+2))
    m,n=len(arr[0]),len(arr)
    cnt=len(storage[0])*len(storage)
    
    for i in range(n):
        for j in range(m):
            dic[arr[i][j]]+=1
    for r in requests:
        con=r[0]
        if con not in dic or dic[con]==0:
            continue
        if len(r)==1:
            지게차(arr,con,m,n)
        elif len(r)==2: 
            크레인(arr,con,m,n)
    return cnt