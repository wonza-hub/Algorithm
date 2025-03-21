import sys
input=sys.stdin.readline

n,m=map(int,input().rstrip().split())

INF=int(1e9)
graph=[[INF]*n for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().rstrip().split())
    graph[a-1][b-1]=1
    graph[b-1][a-1]=1

for i in range(n):
    graph[i][i]=0

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

arr=[]
for s in range(n):
    arr.append((s+1,sum(graph[s])))
    arr.sort(key=lambda x:(x[1],x[0]))

print(arr[0][0])