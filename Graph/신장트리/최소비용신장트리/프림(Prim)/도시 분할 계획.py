import sys
import heapq as hq
input=sys.stdin.readline

min_total_cost=0
n,m=map(int,input().rstrip().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().rstrip().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

ch=[0]*(n+1)
q=[]
hq.heappush(q,(0,1))
max_cost=0

while q:
    cost,v=hq.heappop(q)
    if not ch[v]:
        ch[v]=1
        # 확실히 방문하기로 한 정점이 들어왔으므로, 최대 비용을 초기화
        max_cost=max(max_cost,cost)
        min_total_cost+=cost
        for c,i in graph[v]:
            if not ch[i]:
                hq.heappush(q,(c,i))

print(min_total_cost-max_cost)

