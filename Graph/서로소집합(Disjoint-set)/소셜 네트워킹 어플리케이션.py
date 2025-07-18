import sys
sys.setrecursionlimit(10 ** 6)
input=sys.stdin.readline

def find(p,x):
    if p[x]!=x:
        p[x]=find(p,p[x])
    return p[x]

def uni(p,x,y):
    if x==y:
        return
    x=find(p,x)
    y=find(p,y)
    p[x]=y

for t in range(1,int(input().rstrip())+1):
    print(f'Scenario {t}:')
    n=int(input().rstrip())
    p=[0]*(n+1)
    for i in range(n+1):
        p[i]=i

    k=int(input().rstrip())
    for _ in range(k):
        # 두 친구 간 union 연산 수행
        a,b=map(int,input().rstrip().split())
        uni(p,a,b)

    m=int(input().rstrip())
    for _ in range(m):
        # 두 친구 각각 find 연산 수행
        u,v=map(int,input().rstrip().split())
        if find(p,u)==find(p,v):
            print(1)
        else:
            print(0)
    print()

# 복습 풀이 
import sys
input=sys.stdin.readline


def find(x):
    if p[x]!=x:
        p[x]=find(p[x])
    return p[x]

def uni(x,y):
    if x==y:
        return
    x=find(x)
    y=find(y)
    p[x]=y

for t in range(1,int(input().rstrip())+1):
    print(f'Scenario {t}:')
    n=int(input().rstrip())
    p=[i for i in range(n)]
    for _ in range(int(input().rstrip())):
        a,b=map(int,input().rstrip().split())
        uni(a,b)
    for _ in range(int(input().rstrip())):
        a,b=map(int,input().rstrip().split())
        print(1 if find(a)==find(b) else 0)
    print()
        
    