import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()

def dfs(a,s):
    if len(a)==m:
        print(' '.join(map(str,a)))
        return

    for i in range(s,n):
        dfs(a+[arr[i]],i+1)
    

dfs([],0)