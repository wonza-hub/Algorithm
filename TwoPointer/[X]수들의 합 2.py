# n, m = map(int, input().split())
# seq = list(map(int ,input().split()))
# sum = seq[0]
# cnt = 0
# lp, rp = 0, 1

# while True:
#     if sum < m:
#         if rp < n:
#             sum += seq[rp]
#             rp += 1
#         else:
#             break
#     elif sum == m:
#         cnt += 1
#         sum -= seq[lp]
#         lp += 1
#     else:
#         sum -= seq[lp]
#         lp += 1
        
# print(cnt)

# 복습 풀이
import sys
input=sys.stdin.readline

s,e=0,1
ans=0
n,m=map(int,input().rstrip().split())
arr=list(map(int,input().rstrip().split()))
sum=arr[0] # 누적값을 첫 번째 원소로 초기화

while True:
    if sum<m:
        if e<n:
            sum+=arr[e]
            e+=1
        else:
            break
    else:
        if sum==m:
            ans+=1
        sum-=arr[s]
        s+=1

print(ans)