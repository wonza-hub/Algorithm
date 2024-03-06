n = int(input())
graph = [[] for _ in range(n + 1)]
ch = [0] * (n + 1)

k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    graph[a].append(b)    
    graph[b].append(a)    

def dfs(v):
    for node in graph[v]:
        if ch[node] == 0:
            ch[node] = 1
            dfs(node)

dfs(1)
print(ch[2:].count(1))