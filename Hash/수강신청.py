import sys
input=sys.stdin.readline
from collections import defaultdict

d=defaultdict(int)
k,l=map(int,input().rstrip().split())
arr=[]
for _ in range(l):
    id=input().rstrip()
    d[id]+=1
    arr.append(id)

ans=[]
for a in arr:
    if d[a]==1:
        ans.append(a)
    if d[a]>1:
        d[a]-=1

print(*ans[:k],sep="\n")