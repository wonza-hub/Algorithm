import sys
input=sys.stdin.readline

a,b=[],[]
n,m=map(int,input().rstrip().split())

for _ in range(n):
    d,v=map(int,input().rstrip().split())
    a+=[v]*d
for _ in range(m):
    d,v=map(int,input().rstrip().split())
    b+=[v]*d

ans=0
for i in range(len(b)):
    diff=b[i]-a[i]
    if diff>0:
        ans=max(ans,diff)

print(ans)