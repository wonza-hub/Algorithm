import sys
input=sys.stdin.readline
import heapq as hq

n=int(input().rstrip())
graph=[[] for _ in range(n+1)]
INF=int(1e8)
d=[INF]*(n+1)
m=int(input().rstrip())

def dijkstra(s):
    q=[]
    hq.heappush(q,(0,s))
    d[s]=0

    while q:
        c,now=hq.heappop(q)
        if c>d[now]:
            continue

        for i in graph[now]:
            cost=c+i[1]
            if cost<d[i[0]]:
                d[i[0]]=cost
                hq.heappush(q,(cost,i[0]))

for _ in range(m):
    a,b,cost=map(int,input().rstrip().split())
    graph[a].append((b,cost))
s,e=map(int,input().rstrip().split())
dijkstra(s)
print(d[e])