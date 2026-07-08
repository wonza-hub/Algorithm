# 풀이 참고
import heapq as hq

def dijkstra(board,sx,sy,N):
    ans=int(1e9)
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    
    INF=int(1e9)
    dis = [[[INF]*4 for _ in range(N)] for _ in range(N)]
    q=[]
    hq.heappush(q,(0,sx,sy,-1))
    for i in range(4):
        dis[sx][sy][i]=0
    
    while q:
        dist,x,y,d=hq.heappop(q)
        if x==N-1 and y==N-1:
            ans=min(ans,dist)
            
        if dis[x][y][d if d!=-1 else 0]<dist:
            continue
            
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            # 영역 밖
            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue
            # 벽
            if board[nx][ny]==1:
                continue
            # 시작점이거나 방향이 동일한 경우    
            if d==-1 or d==i:
                new_cost=dist+100
            else:
                new_cost=dist+500+100
                
            if dis[nx][ny][i]>new_cost:
                dis[nx][ny][i]=new_cost
                hq.heappush(q,(new_cost,nx,ny,i))
    return ans

def solution(board):
    answer = 0
    N=len(board[0])
    ans=dijkstra(board,0,0,N)
    
    return ans