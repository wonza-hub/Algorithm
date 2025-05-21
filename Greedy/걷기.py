import sys
input=sys.stdin.readline

x,y,w,s=map(int,input().rstrip().split())
ans=0
if x==0 and y==0:
    ans=0
elif x!=0 and y!=0:
    if 2*w>=s:
        diff=abs(x-y)
        if w<s:
            ans=min(x,y)*s+diff*w
        else:
            ans=min(x,y)*s+diff//2*2*s+diff%2*w
    else:
        ans=(x+y)*w
else:
    if w<s:
        ans=(x+y)*w
    else:
        ans=(x+y)//2*2*s+(x+y)%2*w

print(ans)