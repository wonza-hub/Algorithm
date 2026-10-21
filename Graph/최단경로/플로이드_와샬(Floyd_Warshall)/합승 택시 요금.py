# 플로이드 와샬 풀이
def solution(n, s, a, b, fares):
    INF=int(1e6)
    graph=[[INF]*(n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        graph[i][i]=0
        
    for start,end,cost in fares:
        graph[start][end]=cost
        graph[end][start]=cost
        
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
    
    # 합승 처음부터 안하는 경우
    ans=graph[s][a]+graph[s][b]
    
    # 합승 하는 경우
    for k in range(1,n+1):
        if k==s:
            continue
        ans=min(ans,graph[s][k]+graph[k][a]+graph[k][b])
    
    return ans