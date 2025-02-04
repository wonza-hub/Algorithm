import heapq
INF = int(1e9)

def dijkstra(start, graph, dis):
    q = []
    heapq.heappush(q, (0, start))
    dis[start] = 0
    
    while q:
        time, now = heapq.heappop(q)
        if dis[now] < time:
            continue
            
        for i in graph[now]:
            cost = time + i[1]
            if cost < dis[i[0]]:
                dis[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n + 1)]
    dis = [INF] * (n + 1)
    for road in roads:
        a, b = road
        graph[a].append((b, 1))
        graph[b].append((a, 1))
    
    dijkstra(destination, graph, dis)
    for source in sources:
        comeback_time = -1 if dis[source] == INF else dis[source]
        answer.append(comeback_time)
    
    return answer