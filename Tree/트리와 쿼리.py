import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

n,r,q=map(int,input().rstrip().split())
graph=[[] for _ in range(n+1)]
p=[0]*(n+1)
size=[0]*(n+1)

# dfs를 통해 정점의 부모들을 기록
def find_p(v):
    for i in graph[v]:
        if i==p[v]:
            continue
        p[i]=v
        find_p(i)

# 재귀를 통해 정점의 서브트리의 정점 개수 기록
def count_sub_tree_nodes(v):
    size[v]=1
    for i in graph[v]:
        if i==p[v]:
            continue
        count_sub_tree_nodes(i)
        # 자식 정점 방문 후의 결과를 현재 정점 size에 추가
        size[v]+=size[i]

for _ in range(n-1):
    u,v=map(int,input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

find_p(r)
count_sub_tree_nodes(r)
for _ in range(q):
    print(size[int(input().rstrip())])
