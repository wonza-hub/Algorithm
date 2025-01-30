m,n=map(int,input().split())
arr=list(map(int,input().split()))

def count(l):
    cnt=0
    for a in arr:
        cnt+=a//l

    return cnt

s,e=1,max(arr)
ans=0
while s<=e:
    mid=(s+e)//2
    if count(mid)>=m:
        ans=mid
        s=mid+1
    else:
        e=mid-1
print(ans)