import sys
input=sys.stdin.readline

n,m=map(int,input().rstrip().split())
p=[i for i in range(n)]

def find(p,x):
    if p[x]!=x:
        p[x]=find(p,p[x])
    return p[x]

def uni(p,x,y):
    x=find(p,x)
    y=find(p,y)

    if x<y:
        p[y]=x
    else:
        p[x]=y

for i in range(m):
    a,b=map(int,input().rstrip().split())
    if find(p,a)==find(p,b):
        print(i+1)
        break
    else:
        uni(p,a,b)
else:
    print(0)
