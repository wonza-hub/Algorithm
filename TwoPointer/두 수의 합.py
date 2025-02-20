import sys
input=sys.stdin.readline

n=int(input().rstrip())
arr=list(map(int,input().rstrip().split()))
x=int(input().rstrip())
arr.sort()
ans=0
s,e=0,len(arr)-1

while s<e:
    sum=arr[s]+arr[e]
    if sum==x:
        ans+=1
        s+=1
        e-=1
    elif sum<x:
        s+=1
    else:
        e-=1
print(ans)