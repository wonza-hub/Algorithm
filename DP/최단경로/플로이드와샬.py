INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]


for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a][b] = cost

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
        
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0
        if graph[a][b] == INF:
            graph[a][b] = 'M'
        print(graph[a][b], end = " ")
    print()