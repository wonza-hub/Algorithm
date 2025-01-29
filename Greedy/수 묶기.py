from collections import deque
import sys
input=sys.stdin.readline

n=int(input())
arr=[]
for _ in range(n):
    arr.append(int(input().rstrip()))
arr.sort()

neg=deque([])
pos=[]
for a in arr:
    if a<=0:
        neg.append(a)
    else:
        pos.append(a)

ans=0

while pos and len(pos)!=1:
    ans+=max(pos[-1]*pos[-2],pos[-1]+pos[-2])
    pos.pop()
    pos.pop()
if len(pos)==1:
    ans+=pos[0]

while neg and len(neg)!=1:
    ans+=max(neg[0]*neg[1],neg[0]+neg[1])
    neg.popleft()
    neg.popleft()
if len(neg)==1:
    ans+=neg[0]

print(ans)
