import sys
input=sys.stdin.readline

INF=int(1e9)

n,m=map(int,input().rstrip().split())
edges=[]
d=[INF]*(n+1)

def bellman_ford(s):
    # 시작 노드에 대해 초기화
    d[s]=0
    # 전체 n번의 라운드를 반복
    for i in range(n):
        # 매 라운드마다 모든 간선을 확인
        for j in range(m):
            cur,next_node,cost=edges[j]
            if d[cur]!=INF and d[next_node]>d[cur]+cost:
                d[next_node]=d[cur]+cost
                if i==n-1:
                    return True
    return False

for _ in range(m):
    a,b,c=map(int,input().rstrip().split())
    edges.append((a,b,c))

negative_cycle=bellman_ford(1)

if negative_cycle:
    print('-1')
else:
    for i in range(2,n+1):
        if d[i]==INF:
            print('-1')
        else:
            print(d[i])