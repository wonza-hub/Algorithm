import sys
input=sys.stdin.readline
from collections import Counter

n,m=map(int,input().rstrip().split())
arr=[]
for _ in range(n):
    s=input().rstrip()
    if len(s)<m:
        continue
    arr.append(s)

tmp=Counter(arr).most_common()
tmp.sort(key=lambda x:(-x[1],-len(x[0]),x[0]))
for x,y in tmp:
    print(x)
