# 계수 정렬
import sys
input=sys.stdin.readline

n=int(input().rstrip())
arr=[0]*(10000+1)
for _ in range(n):
    arr[int(input().rstrip())]+=1

for i in range(len(arr)):
    if arr[i]:
        for _ in range(arr[i]):
            print(i)
