import sys
input=sys.stdin.readline

n=int(input().rstrip())
MAX=1_000_000
tmp=[0]*(2*MAX+1)

for _ in range(n):
    tmp[int(input().rstrip())+MAX]+=1
    
for i in range(2*MAX+1):
    for _ in range(tmp[i]):
        print(i-MAX)

