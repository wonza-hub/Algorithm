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