import sys
input=sys.stdin.readline

n,m=map(int,input().rstrip().split())
arr=list(map(int,input().rstrip().split()))
arr.sort()

ch=[0]*n

res=[]
def dfs(s):
    if len(res)==m:
        print(' '.join(map(str,res)))
        return
    for i in range(n):
        if ch[i]:
            continue
        res.append(arr[i])
        ch[i]=1
        dfs(i+1)
        res.pop()
        ch[i]=0

dfs(0)