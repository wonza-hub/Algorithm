import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))
arr.sort()
ans=1

for i in range(2,max(arr)+1):
    cnt=0
    for ar in arr:
        if ar%i==0:
            cnt+=1
    ans=max(ans,cnt)

print(ans)