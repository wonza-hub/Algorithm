import sys
input=sys.stdin.readline

n,m=map(int,input().split())
d={}
arr=[0]*(n+1)

for i in range(1,n+1):
    name=input().rstrip()
    d[name]=i
    arr[i]=name

for _ in range(m):
    p=input().rstrip()
    if p.isdigit():
        print(arr[int(p)])
    else:
        print(d[p])