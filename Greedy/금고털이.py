import sys
input=sys.stdin.readline

w,n=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]

arr.sort(key=lambda x: -x[1])

tv=0
for gw,gv in arr:
    if gw<=w:
        tv+=gw*gv
        w-=gw
    else:
        tv+=w*gv
        break

print(tv)