from collections import deque 

def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    dis = [-1] * (n + 1)
    
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    
    q = deque([1])
    dis[1] = 0
    
    while q:
        now = q.popleft()
        for i in graph[now]:
            if dis[i] == -1:
                q.append(i)
                dis[i] = dis[now] + 1
                    
    return dis.count(max(dis))
        

# 복습 풀이
# 노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex
# 1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return 
# 간선은 양방향

from collections import deque

def solution(n, edge):
    q = deque([1])
    graph = [[] for _ in range(n + 1)]
    dis = [-1] * (n + 1)
    dis[1] = 0
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
        
    while q:
        cur = q.popleft()
        for next in graph[cur]:
            if dis[next] == -1:
                dis[next] = dis[cur] + 1
                q.append(next)
    
    return dis.count(max(dis))
                    
        
    