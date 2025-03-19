import sys
input=sys.stdin.readline
from bisect import bisect_left

def solution(a,b):
    a.sort()
    b.sort()
    cnt=0
    for aa in a:
        i=bisect_left(b,aa)
        cnt+=i

    return cnt

for _ in range(int(input().rstrip())):
    n,m=map(int,input().rstrip().split())
    a=list(map(int,input().rstrip().split()))
    b=list(map(int,input().rstrip().split()))
    print(solution(a,b))