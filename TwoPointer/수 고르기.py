import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(int(input()))
arr.sort()
l,r=0,0
cnt=0
ans=20e9

while True:
    if r>=n or l>=n:
        break
    diff=arr[r]-arr[l]
    if diff<m:
        r+=1
    elif diff>=m:
        l+=1
        ans=min(ans,diff)
print(ans)