import sys
input=sys.stdin.readline
from math import sqrt

s=input().rstrip()
l=len(s)
r,c=1,l
for i in range(1,int(sqrt(l))+1):
    if l%i==0:
        r,c=i,l//i

for j in range(0,r):
    for k in range(j,l,r):
        print(s[k],end='')
    