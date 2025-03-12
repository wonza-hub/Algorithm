from collections import deque
import sys
input=sys.stdin.readline

n,w,l=map(int,input().rstrip().split())
arr=list(map(int,input().rstrip().split()))

t=deque(arr)
q=deque([0]*w)
tw,ans=0,0

def enter():
    global tw
    if l<tw+t[0]:
        return
    x=t.popleft()
    q[-1]=x
    tw+=x

def exit():
    global tw
    if q[0]:
        tw-=q[0]
        q[0]=0

while t:
    ans+=1
    enter()
    exit()
    q.rotate(-1)

print(ans+w)
