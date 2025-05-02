import sys
input=sys.stdin.readline

for _ in range(int(input().rstrip())):
    n=int(input().rstrip())
    coins=list(map(int,input().rstrip().split()))
    t=int(input().rstrip())
    d=[0]*(t+1)
    d[0]=1

    for c in coins:
        for i in range(c,t+1):
            d[i]+=d[i-c]
    print(d[t])

# 2차원 풀이
import sys
input=sys.stdin.readline

for _ in range(int(input().rstrip())):
    n=int(input().rstrip())
    coin=[0]+list(map(int,input().rstrip().split()))
    t=int(input().rstrip())
    d=[[0]*(t+1) for _ in range(n+1)]

    for k in range(n+1):
        d[k][0]=1

    for i in range(1,n+1):
        for j in range(1,t+1):
            d[i][j]+=d[i-1][j]
            if j-coin[i]>=0:
                d[i][j]+=d[i][j-coin[i]]
    print(d[n][t])

