import sys
input=sys.stdin.readline

a=int(input().rstrip())
b=int(input().rstrip())
c=int(input().rstrip())

res=a*b*c
res=list(map(int,str(res)))

for i in range(10):
    print(res.count(i))
