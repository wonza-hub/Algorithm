import sys
input=sys.stdin.readline
from collections import defaultdict

n,m,k=map(int,input().split())
cost=[0]+list(map(int,input().split()))
p=[i for i in range(n+1)]

def find(x):
    if p[x]!=x:
        p[x]=find(p[x])
    return p[x]

def union(x,y):
    x=find(x)
    y=find(y)
    # 친구비가 적은 것이 부모가 됨 
    if cost[x]<cost[y]:
        p[y]=x
    else:
        p[x]=y

for _ in range(m):
    v,w=map(int,input().split())
    union(v,w)

friends=set()
res=0
for i in range(1,n+1):
    # 친구의 부모가 이미 확인한 부모와 겹치지 않은 경우
    if find(i) not in friends:
        res+=cost[p[i]]
        friends.add(p[i])

if res>k:
    print("Oh no")
else:
    print(res)
