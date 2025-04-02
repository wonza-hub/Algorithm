import sys
input=sys.stdin.readline

s=list(input().rstrip())
s=list(map(ord,s))

for o in range(ord('a'),ord('z')+1):
    c=s.count(o)
    print(c,end=" ")
