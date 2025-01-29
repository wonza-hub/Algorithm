import sys
input = sys.stdin.readline

n=int(input())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))

arr.sort(key=lambda x:x[0])

ts,te=arr[0][0],arr[0][1]
ans=0

for s,e in arr:
    if te>=s:
        te=max(te,e)
    else:
        ans+=abs(te-ts)
        te,ts=e,s

ans+=abs(te-ts)
print(ans)
