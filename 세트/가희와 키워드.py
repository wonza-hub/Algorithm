import sys
input=sys.stdin.readline

n,m=map(int,input().rstrip().split())
memo=set()
for _ in range(n):
    memo.add(input().rstrip())
for _ in range(m):
    a=set(input().rstrip().split(','))
    memo-=a
    print(len(memo))
