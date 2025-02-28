import sys
input=sys.stdin.readline

n,m=map(int,input().rstrip().split())
p=[i for i in range(n+1)]

def find(p,x):
    if p[x]!=x:
        p[x]=find(p,p[x])
    return p[x]

def uni(p,a,b):
    a=find(p,a)
    b=find(p,b)
    if a<b:
        p[b]=a
    else:
        p[a]=b

set_count=set()
cycle=0
for _ in range(m):
    u,v=map(int,input().rstrip().split())
    if find(p,u)==find(p,v):
        cycle+=1
    uni(p,u,v)

for i in range(1, n + 1):
    set_count.add(find(p,i))
# print(cycle+len(set(p[1:]))-1) # 오답
print(cycle + len(set_count) - 1)