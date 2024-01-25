# 방법 1
n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

# 방법 2
n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n
res = 0

for i in range(1, n):
    max = 0
    for j in range(0, i):
        if arr[j] < arr[i] and dp[j] > max:
            max = dp[j]
    dp[i] = max + 1
    if dp[i] > res:
        res=dp[i]
        
print(res)