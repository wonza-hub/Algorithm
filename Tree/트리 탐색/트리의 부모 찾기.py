import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

n=int(input())
graph=[[] for _ in range(n+1)]
p=[0]*(n+1)

def dfs(v):
    for i in graph[v]:
        # 방문했더니 나의 부모인 경우는 무시
        if p[v]==i:
            continue
        p[i]=v
        dfs(i)


for _ in range(n-1):
    u,v=map(int,input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(1)
for i in range(2,n+1):
    print(p[i])
