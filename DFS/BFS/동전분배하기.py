n = int(input())
sum = [0] * 3
min_diff = 10e9
coins = []
for _ in range(n):
    coins.appned(int(input()))

def dfs(l):
    global min_diff
    if l == n:
        if len(set(sum)) == 3:
            min_diff = min(min_diff, max(sum) - min(sum))
    else:
        for i in range(len(sum)):
            sum[i] += coins[l]
            dfs(l + 1)
            sum[i] -= coins[l]

dfs(0)
print(min_diff)