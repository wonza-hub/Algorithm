import sys
input=sys.stdin.readline

s=input().rstrip()
t=input().rstrip()
step=len(t)

ans=0
i=0
while True:
    if i>=len(s):
        break

    idx=s.find(t,i)

    if idx!=-1:
        ans+=1
        i=idx+step
    else:
        break
print(ans)