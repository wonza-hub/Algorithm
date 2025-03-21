import sys
input=sys.stdin.readline

arr=[]
n=int(input().rstrip())
for _ in range(n):
    arr.append(tuple(map(int,input().rstrip().split())))

ans=int(1e9)
def dfs(l,s,b):
    global ans
    if l==n:
        if s==1 and b==0:
            return
        ans=min(ans,abs(s-b))
        return
    dfs(l+1,s*arr[l][0],b+arr[l][1])
    dfs(l+1,s,b)

dfs(0,1,0)
print(ans)