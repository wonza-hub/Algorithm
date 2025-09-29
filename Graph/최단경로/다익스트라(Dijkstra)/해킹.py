import sys
input=sys.stdin.readline
import heapq as hq

INF=int(1e9)

def dijkstra(start,graph):
    d=[INF]*(n+1)
    d[start]=0
    q=[]
    hq.heappush(q,(0,start))
    cnt=0
    while q:
        time,now=hq.heappop(q)
        last=now
        if d[now]<time:
            continue
        cnt+=1
        for next,t in graph[now]:
            cost=time+t
            if cost<d[next]:
                d[next]=cost
                hq.heappush(q,(cost,next))

    # 마지막에 도달한 정점이 반드시 최소시간이라는 보장은 없음에 유의
    tmp=[x for x in sorted(list(set(d[1:]))) if x!=INF]

    return [cnt,tmp[-1]]

for _ in range(int(input().rstrip())):
    n,d,c=map(int,input().rstrip().split())
    graph=[[] for _ in range(n+1)]
    for _ in range(d):
        a,b,s=map(int,input().rstrip().split())
        graph[b].append((a,s))
    [cnt,total_t]=dijkstra(c,graph)
    print(cnt,total_t)