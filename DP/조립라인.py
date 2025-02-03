import sys
input=sys.stdin.readline

n=int(input())
a=[0]*n
b=[0]*n
atob=[0]*(n-1)
btoa=[0]*(n-1)
da=[0]*n
db=[0]*n

for i in range(n):
    if i==n-1:
        a[i],b[i]=map(int,input().split())
    else:
        a[i],b[i],atob[i],btoa[i]=map(int,input().split())

da[0],db[0]=a[0],b[0]
for i in range(1,n):
    da[i]=min(a[i]+db[i-1]+btoa[i-1],a[i]+da[i-1])
    db[i]=min(b[i]+da[i-1]+atob[i-1],b[i]+db[i-1])
print(min(da[n-1],db[n-1]))