import sys
input=sys.stdin.readline
from collections import deque

s=int(input().rstrip())
q=deque([[0,0,1]])
ch=[[0]*1001 for _ in range(1001)]
ch[1][0]=1

while q:
    t,clip,cnt=q.popleft()
    if cnt==s:
        print(t)
        break

    if 0<=cnt<=1000 and 0<=clip<=1000 and not ch[clip][cnt]:
        ch[clip][cnt]=1
        q.append([t+1,cnt,cnt])
        q.append([t+1,clip,cnt+clip])
        q.append([t+1,clip,cnt-1])