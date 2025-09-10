import sys
input=sys.stdin.readline


def isFriend(l1,l2):
    s1,e1=l1
    s2,e2=l2
    if s1<=s2:
        if e1>=s2:
            return True
    else:
        if s1<=e2:
            return True
    return False


n=int(input().rstrip())
arr=[]
INF=int(1e9)
graph=[[INF]*n for _ in range(n)]
for _ in range(n):
    s,e=map(int,input().rstrip().split())
    arr.append((s,e))

for i in range(n):
    for j in range(i+1,n):
        if isFriend(arr[i],arr[j]):
            graph[i][j]=1
            graph[j][i]=1

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

q=int(input().rstrip())
for _ in range(q):
    l1,l2=map(int,input().rstrip().split())
    if graph[l1-1][l2-1]==INF:
        print(-1)
    else:
        print(graph[l1-1][l2-1])

