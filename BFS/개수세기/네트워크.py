from collections import deque

def bfs(x, n, computers, ch):
    q = deque([x])
    while q:
        com = q.popleft()
        ch[com] = 1
        for another_com in range(n):
            if another_com != com and ch[another_com] == 0:
                if computers[com][another_com] == 1:
                    q.append(another_com)

def solution(n, computers):
    answer = 0
    ch = [0] * n
    for i in range(n):
        if not ch[i]:
            bfs(i, n, computers, ch)
            answer += 1

    return answer

# 복습 풀이
# UNION-FIND로 풀이
def find(x,p):
    if p[x]!=x:
        p[x]=find(p[x],p)
    return p[x]
    
def union(a,b,p):
    a=find(a,p)
    b=find(b,p)
    if a>b:
        p[a]=b
    else:
        p[b]=a
     
def solution(n, computers):
    answer = 0
    p=[i for i in range(n)]
    for i in range(len(computers)):
        for j in range(len(computers[0])):
            if i==j:
                continue
            if computers[i][j]==1:
                union(i,j,p)
                
    return len(set(find(i,p) for i in range(n)))