import heapq as hq

n,m=map(int,input().split())
arr=list(map(int,input().split()))
hq.heapify(arr)

acc=sum(arr)
for _ in range(m):
    a=hq.heappop(arr)
    b=hq.heappop(arr)
    tmp=a+b
    a,b=tmp,tmp
    acc+=tmp
    hq.heappush(arr,a)
    hq.heappush(arr,b)

print(acc)