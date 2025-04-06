import sys
input=sys.stdin.readline

n,k=map(int,input().rstrip().split())
arr=[[0]*2 for _ in range(6)]
for _ in range(n):
    s,y=map(int,input().rstrip().split())
    arr[y-1][s]+=1

ans=0
for i in range(6):
    for j in range(2):
        tmp=arr[i][j]
        # 나머지가 남는 경우: 방 하나 더 추가
        if tmp%k:
            ans+=tmp//k+1
        # 나머지가 없는 경우: 몫만큼의 방 필요
        else:
            ans+=tmp//k
print(ans)