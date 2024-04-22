import sys
import heapq as hq
input = sys.stdin.readline

max_heap = []
n = int(input())
for _ in range(n):
    cmd = int(input())
    if cmd == 0:
        print((-1) * hq.heappop(max_heap) if max_heap else 0)
    else:
        hq.heappush(max_heap, (-1) * cmd)