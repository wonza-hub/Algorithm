import sys
sys.setrecursionlimit(5000)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
ans = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    visited[v] = True
    for j in graph[v]:
        if not visited[j]:
            dfs(j)

for i in range(1, n + 1):
    if not visited[i]:
        ans += 1
        dfs(i)

print(ans)
