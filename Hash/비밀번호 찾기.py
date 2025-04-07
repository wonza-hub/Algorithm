import sys
input=sys.stdin.readline
from collections import defaultdict

d=defaultdict(str)
n,m=map(int,input().rstrip().split())

for _ in range(n):
    ad,pw=input().rstrip().split()
    d[ad]=pw

for _ in range(m):
    ad=input().rstrip()
    print(d[ad])