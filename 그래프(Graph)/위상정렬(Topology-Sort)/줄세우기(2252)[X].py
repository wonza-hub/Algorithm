from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = []
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end = " ")

topology_sort()

# 복습 풀이
from collections import deque

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
indegree=[0]*(n+1)

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    indegree[b]+=1
    
def depology_sort():
    result=[]
    q=deque()
    for i in range(1,n+1):
        if not indegree[i]:
            q.append(i)
    while q:
        v=q.popleft()
        result.append(v)
        for w in graph[v]:
            indegree[w]-=1
            if not indegree[w]:
                q.append(w)
                
    for i in result:
        print(i,end=' ')

depology_sort()