import sys
input=sys.stdin.readline

n,m=map(int,input().rstrip().split())
arr=list(map(int,input().rstrip().split()))
arr.sort()

def dfs(a,l):
    if l==m:
        print(' '.join(map(str,a)))
        return
    
    for i in range(n):
        dfs(a+[arr[i]],l+1)

dfs([],0)