import sys
input=sys.stdin.readline
import heapq as hq

n,e=map(int,input().rstrip().split())
graph=[[] for _ in  range(n+1)]
INF=int(1e9)

for _ in range(e):
    a,b,c=map(int,input().rstrip().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
v1,v2=map(int,input().rstrip().split())

def dijkstra(s,e):
    d=[INF]*(n+1)
    q=[]
    hq.heappush(q,(0,s))
    d[s]=0

    while q:
        c,now=hq.heappop(q)
        if c>d[now]:
            continue
        for v,co in graph[now]:
            cost=c+co
            if cost<d[v]:
                d[v]=cost
                hq.heappush(q,(cost,v))
    
    return d[e]

x=dijkstra(1,v1)+dijkstra(v1,v2)+dijkstra(v2,n)
y=dijkstra(1,v2)+dijkstra(v2,v1)+dijkstra(v1,n)
if x>=INF and y>=INF:
    print(-1)
else:
    print(min(x,y))


