import heapq as hq
import sys
input=sys.stdin.readline

INF=int(1e5)
dx=[-1,0,1,0]
dy=[0,1,0,-1]

m,n=map(int,input().rstrip().split())
d=[[INF]*m for _ in range(n)]
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().rstrip())))

def dijkstra(sc,sx,sy):
    q=[]
    hq.heappush(q,(sc,(sx,sy)))
    d[sx][sy]=sc

    while q:
        c,(x,y)=hq.heappop(q)
        if c>d[x][y]:
            continue

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                cost=c+arr[nx][ny]

                if cost<d[nx][ny]:
                    d[nx][ny]=cost
                    hq.heappush(q,(d[nx][ny],(nx,ny)))

dijkstra(0,0,0)
print(d[n-1][m-1])
