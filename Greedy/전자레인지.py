import sys
input=sys.stdin.readline

t=int(input().rstrip())
btn=[300,60,10]
ans=[0]*3

for i in range(3):
    ans[i]+=t//btn[i]
    t%=btn[i]

if t==0:
    print(*ans)
else:
    print(-1)
