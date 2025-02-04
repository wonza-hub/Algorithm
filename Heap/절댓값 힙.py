import sys
import heapq as hq
input=sys.stdin.readline

heap=[]
n=int(input().rstrip())

for _ in range(n):
    v=int(input())
    if v:
        hq.heappush(heap,(abs(v),v))
    else:
        if heap:
            print(hq.heappop(heap)[1])
        else:
            print(0)
