import math
import heapq as hq
import sys
input=sys.stdin.readline

n=int(input())
graph=[[] for _ in range(n+1)]
d=[math.inf]*(n+1)
pre=[0]*(n+1)

m=int(input())
for _ in range(m):
    a,b,cost=map(int,input().split())
    graph[a].append((b,cost))
start,end=map(int,input().split())

def dijkstra(s):
    q=[]
    d[s]=0
    hq.heappush(q,(0,s))

    while q:
        cur_c,cur=hq.heappop(q)

        if d[cur]<cur_c:
            continue

        for v,c in graph[cur]:
            cost=cur_c+c
            if d[v]>cost:
                d[v]=cost
                hq.heappush(q,(cost,v))
                # 이전 정점을 기록 
                pre[v]=cur

dijkstra(start)

# 경로 복원 
path=[]
tmp=end
while(tmp!=start):
    path.append(tmp)
    tmp=pre[tmp]
path.append(tmp)

print(d[end])
print(len(path))
print(' '.join(map(str,reversed(path))))