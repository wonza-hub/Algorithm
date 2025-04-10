import sys
input=sys.stdin.readline
import heapq as hq

for _ in range(int(input())):
  k = int(input())
  files = list(map(int,input().split()))
  hq.heapify(files)
  ans=0

  while len(files)>1:
    tmp=0
    a=hq.heappop(files)
    b=hq.heappop(files)
    tmp+=a+b
    ans+=tmp
    hq.heappush(files, tmp)
  
  print(ans)