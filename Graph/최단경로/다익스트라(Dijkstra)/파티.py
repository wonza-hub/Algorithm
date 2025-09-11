import heapq as hq
import sys
input=sys.stdin.readline

n,m,x=map(int,input().rstrip().split())
graph=[[] for _ in range(n+1)]
INF=int(1e9)
dis=[[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    s,e,c=map(int,input().rstrip().split())
    graph[s].append((e,c))


def dijkstra(start):
    q=[]
    dis[start][start]=0
    hq.heappush(q,(0,start))

    while q:
        cost,x=hq.heappop(q)
        if dis[start][x]<cost:
            continue

        for e,c in graph[x]:
            new_cost=cost+c
            if new_cost<dis[start][e]:
                dis[start][e] = new_cost
                hq.heappush(q, (new_cost, e))


for i in range(1,n+1):
    dijkstra(i)

tmp=[0]*(n+1)
for i in range(1,n+1):
    tmp[i]=dis[i][x]+dis[x][i]
print(max(tmp))
