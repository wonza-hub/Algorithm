import sys
input=sys.stdin.readline
from collections import Counter

s=input().rstrip()
cd=Counter(s.upper())
mc=cd.most_common()
if len(mc)==1:
    print(mc[0][0])
else:
    print('?' if mc[0][1]==mc[1][1] else mc[0][0])