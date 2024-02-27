import heapq

INF = int(1e9)

def solution(n, road, k):
    answer = 0
    
    dis = [INF] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
    q = []
    heapq.heappush(q, (0, 1))
    dis[1] = 0
    
    while q:
        time, now = heapq.heappop(q)
        if time > dis[now]:
            continue
        
        for e, t  in graph[now]:
            time_sum = time + t
            if time_sum < dis[e]:
                dis[e] = time_sum
                heapq.heappush(q, (time_sum, e))
    
    for i in range(1, n + 1):
        if dis[i] <= k:
            answer += 1
            
    return answer