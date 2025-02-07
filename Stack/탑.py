import sys
input=sys.stdin.readline

n=int(input().rstrip())
arr=[0]+list(map(int,input().rstrip().split()))
stack=[]
ans=[0]*(n+1)

# 탑을 역순으로 탐색
for i in range(len(arr)-1,0,-1):
    while stack and arr[i]>stack[-1][0]:
        _,loc=stack.pop()
        ans[loc]=i
    stack.append((arr[i],i))

print(' '.join(map(str, ans[1:])))