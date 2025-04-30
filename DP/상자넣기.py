import sys
input=sys.stdin.readline

n=int(input().rstrip())
arr=list(map(int,input().rstrip().split()))
d=[1]*n

for i in range(n):
    for j in range(i):
        if arr[i]>arr[j]:
            d[i]=max(d[i],d[j]+1)

print(max(d))