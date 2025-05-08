import sys
from collections import deque
input=sys.stdin.readline

str=list(input().rstrip())
q=deque()
ans=''
ch=False

for s in str:
    if s=='<':
        ch=True
        while q:
            ans+=q.pop()
    
    if s==' ' and ch==False:
        while q:
            ans+=q.pop()
        ans+=' '
        continue
    q.append(s)
    if s=='>':
        ch=False
        while q:
            ans+=q.popleft()
if q:
    while q:
        ans+=q.pop()

print(ans)
    
