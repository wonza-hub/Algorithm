# 내 풀이: 완전 탐색
from collections import deque

dx=[1,0,0,-1]
dy=[0,-1,1,0]
dr=['d','l','r','u']
INF=int(1e9)

def solution(n, m, x, y, r, c, k):
    answer = []
    graph=[[0]*(m+1) for _ in range(n+1)]
    dp=[[INF]*(m+1) for _ in range(n+1)]
    q=deque()
    q.append((x,y,''))
    
    while q:
        a,b,route=q.popleft()
        rlen=len(route)
        if rlen>k:
            return 'impossible'
        if dp[a][b]==rlen:
            continue
        dp[a][b]=rlen
        
        # 탈출 지점에 도달한 경우
        if a==r and b==c and len(route)==k:
            answer.append(route)
            break
            
        for i in range(4):
            na=a+dx[i]
            nb=b+dy[i]
            if na>n or nb>m or na<=0 or nb<=0:
                continue
            q.append((na,nb,route+dr[i]))
            
    return ''.join(answer)

# 모범 풀이: Greedy
dx=[1,0,0,-1]
dy=[0,-1,1,0]
dr=['d','l','r','u']

def solution(n, m, x, y, r, c, k):
    dist = abs(x - r) + abs(y - c) # 맨허튼 거리
    
    # 도달 불가 조건
    if dist > k or (k - dist) % 2 == 1:
        return "impossible"
    
    result = []
    for _ in range(k):
        # 사전순: d → l → r → u
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx < 1 or nx > n or ny < 1 or ny > m:
                continue
            remaining = k - len(result) - 1
            new_dist = abs(nx - r) + abs(ny - c)
            if new_dist <= remaining and (remaining - new_dist) % 2 == 0:
                result.append(dr[i])
                x, y = nx, ny
                break
    
    return ''.join(result)
