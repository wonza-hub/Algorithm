import sys
input=sys.stdin.readline

n=int(input().rstrip())
graph=[list(map(int,input().rstrip().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] and graph[k][j]:
                graph[i][j]=1

for r in graph:
    print(*r)
