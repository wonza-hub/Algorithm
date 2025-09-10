import sys
input=sys.stdin.readline

arr=[[0]*100 for _ in range(100)]
n=int(input().rstrip())
for _ in range(n):
    x,y=map(int,input().rstrip().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            arr[i][j]=1
ans=sum(sum(row) for row in arr)
print(ans)