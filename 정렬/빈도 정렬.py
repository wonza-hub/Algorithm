import sys
input=sys.stdin.readline
from collections import Counter

n,c=map(int,input().rstrip().split())
a=list(map(int,input().rstrip().split()))
cd=Counter(a)

tmp=cd.most_common()
tmp=[[x]*y for x,y in tmp]
ans=[]
for t in tmp:
    ans.extend(t)

print(' '.join(list(map(str,ans))))