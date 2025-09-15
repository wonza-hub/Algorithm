import sys
input=sys.stdin.readline

n=int(input().rstrip())
m=int(input().rstrip())
graph=[[0]*(n+1)]
for _ in range(n):
    graph.append([0]+list(map(int,input().rstrip().split())))
plan=list(map(int,input().rstrip().split()))

def find_p(x):
    if p[x]!=x:
        p[x]=find_p(p[x])
        return p[x]
    return x

def union_p(x,y):
    x=find_p(x)
    y=find_p(y)
    if x<y:
        p[y]=x
    else:
        p[x]=y

p=[i for i in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j]==1:
            union_p(i,j)

ans='YES'
for i in range(1,len(plan)):
    if find_p(plan[0])!=find_p(plan[i]):
        ans='NO'
        break
print(ans)