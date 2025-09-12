import sys
input=sys.stdin.readline

n,m,k=map(int,input().rstrip().split())
tmp=list(map(int,input().rstrip().split()))
is_yny=[0]*(n+1)

edges=[]
for _ in range(m):
    u,v,w=map(int,input().rstrip().split())
    edges.append((w,u,v))
edges.sort()
p=[i for i in range(n+1)]
# 부모를 0으로 만들어서 발전소를 루트로 강제로 만들기
for t in tmp:
    p[t]=0

def find_p(x):
    if p[x]!=x:
        p[x]=find_p(p[x])
    return p[x]

def union_p(x,y):
    x=find_p(x)
    y=find_p(y)
    if x<y:
        p[y]=x
    else:
        p[x]=y

ans=0
for e in edges:
    w,u,v=e
    if find_p(u)!=find_p(v):
        union_p(u,v)
        ans+=w
print(ans)