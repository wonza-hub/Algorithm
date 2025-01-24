INF=1e9
n,k=map(int,input().split())
coin=set()
for _ in range(n):
    coin.add(int(input()))

d=[0]+[INF]*k

for c in coin:
    for i in range(c,k+1):
        d[i]=min(d[i],d[i-c]+1)

if d[k]==INF:
    print(-1)
else:
    print(d[k])

