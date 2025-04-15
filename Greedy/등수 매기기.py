import sys
input=sys.stdin.readline

arr=[]
n=int(input().rstrip())
for _ in range(n):
    arr.append(int(input().rstrip()))
arr.sort()

tmp=[i for i in range(1,n+1)]
ans=sum([abs(arr[i]-tmp[i]) for i in range(n)])
print(ans)