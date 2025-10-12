import sys
input=sys.stdin.readline

n=int(input().rstrip())
res=[0]*n
flag=False

def is_bad(l):
    for i in range(1,l//2+2):
        s=l-i+1
        if len(res[s-i:s])!=0 and res[s-i:s]==res[s:l+1]:
            return True
    return False

def dfs(l):
    global flag
    if flag:
        return
    if l==n:
        print(''.join(map(str,res)))
        flag=True
        return
    else:
        for i in range(1,4):
            res[l]=i
            if is_bad(l):
                res[l]=0
                continue
            dfs(l+1)

dfs(0)