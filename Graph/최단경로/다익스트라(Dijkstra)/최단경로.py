import heapq as hq
import sys
input=sys.stdin.readline

V,E=map(int,input().rstrip().split())
k=int(input().rstrip())
graph=[[] for _ in range(V+1)]
INF=300000
d=[INF]*(V+1)

def dijkstra(s):
    # 시작점에 대해 초기화 작업 수행
    q=[]
    hq.heappush(q,(0,s))
    d[s]=0

    # 알고리즘 수행
    while q:
        c,now=hq.heappop(q)
        if c>d[now]:
            continue

        for i in graph[now]:
            cost=c+i[1]
            if cost<d[i[0]]:
                d[i[0]]=cost
                hq.heappush(q,(cost,i[0]))

for _ in range(E):
    u,v,w=map(int,input().rstrip().split())
    graph[u].append((v,w))

dijkstra(k)

for i in range(1,V+1):
    print(d[i] if d[i]!=INF else 'INF')