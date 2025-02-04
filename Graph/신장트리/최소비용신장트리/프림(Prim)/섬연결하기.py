import heapq as hq

def solution(n, costs):
    answer = 0
    ch = [0] * n
    graph = [[0] * n for _ in range(n)]
    
    q = []
    hq.heappush(q, (0, 0))
    for s, e, c in costs:
        graph[s][e] = c
        graph[e][s] = c
    
    while q:
        cost, v = hq.heappop(q) 
        if not ch[v]:
            ch[v] = 1
            answer += cost
            for i in range(n):
                if graph[v][i] != 0 and not ch[i]:
                    hq.heappush(q, (graph[v][i], i))
            
    return answer