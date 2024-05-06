n, k = map(int, input().split())
coins = []

for _ in range(n):
    coin = int(input())
    coins.append(coin)
    
cnt = 0
for i in range(len(coins) - 1, -1, -1):
    if coins[i] > k:
        continue
    cnt += k // coins[i]
    k = k % coins[i]
    if k == 0: 
        break
        
print(cnt)