import sys
input=sys.stdin.readline

arr=[]
n=int(input().rstrip())
for _ in range(n):
    arr.append(int(input().rstrip()))

stack=[]
ans=0
for a in arr:
    while stack and stack[-1]<=a:
        stack.pop()
    stack.append(a)

    ans+=len(stack)-1

print(ans)