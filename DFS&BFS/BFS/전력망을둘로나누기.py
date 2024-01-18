from collections import deque

def bfs(cut, n, graph):
    check = [0] * (n + 1)
    check[cut[0]] = 1
    check[cut[1]] = 1
    
    q = deque()
    q.append(cut[0])
    cnt = 1
    while q:
        x = q.popleft()
        for i in graph[x]:
            if check[i] == 0:
                cnt += 1
                check[i] = cnt
                q.append(i)
                
    return cnt
    
def solution(n, wires):
    ans = 10e9
    graph = [[] for _ in range(n + 1)]
    for w in wires:
        graph[w[0]].append(w[1])
        graph[w[1]].append(w[0])
    
    for i in wires:
        cnt = bfs(i, n, graph)
        
        ans = min(ans, abs(cnt - (n - cnt)))
        
    return ans