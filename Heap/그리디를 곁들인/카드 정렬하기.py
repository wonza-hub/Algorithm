import heapq as hq
import sys
input=sys.stdin.readline

n=int(input().rstrip())
heap=[]
ans=0

for _ in range(n):
    hq.heappush(heap,int(input()))

while len(heap)>1:
    a=hq.heappop(heap)
    b=hq.heappop(heap)
    sum=a+b
    ans+=sum
    hq.heappush(heap,sum)

print(ans)