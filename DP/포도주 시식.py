n=int(input())
d=[0]*10001
arr=[0]*10001

for i in range(1,n+1):
    arr[i]=int(input())

d[1]=arr[1]
d[2]=arr[1]+arr[2]

for i in range(3,n+1):
    # 안 마시는 경우도 포함함에 유의
    d[i]=max(d[i-2]+arr[i],d[i-3]+arr[i-1]+arr[i],d[i-1])

print(max(d))

# 복습 풀이
import sys
input=sys.stdin.readline

n=int(input().rstrip())
## 인덱스 런타임 에러를 방지하기 위해 문제 조건에 맞게 공간을 확보
arr=[0]*10001
d=[0]*10001

## dp의 조건식에 맞게 인덱스 범위가 벗어나지 않도록 초기화에 유의
for i in range(1,n+1):
    arr[i]=int(input().rstrip())

d[1]=arr[1]
d[2]=arr[1]+arr[2]

for i in range(3,n+1):
    d[i]=max(d[i-3]+arr[i]+arr[i-1],d[i-2]+arr[i],d[i-1])

print(max(d))