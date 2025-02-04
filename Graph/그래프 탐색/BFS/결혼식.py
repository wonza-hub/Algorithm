import sys
from collections import deque
input=sys.stdin.readline

n=int(input().rstrip())
m=int(input().rstrip())
graph=[[] for _ in range(n+1)]
ch=[0]*(n+1)
ch[1]=1
ans=0

def bfs(v,d):
    global ans
    if d==2:
        return
    for i in graph[v]:
        if not ch[i]:
            ch[i]=1
            ans+=1
            q.append((i,d+1))

for _ in range(m):
    a,b=map(int,input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

q=deque()
q.append((1,0))
while q:
    p,d=q.popleft()
    bfs(p,d)

print(ans)