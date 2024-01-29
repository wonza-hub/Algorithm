ans = 0

n = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

min_cost = cost[0]
for i in range(n - 1):
    min_cost = min(min_cost, cost[i])
    ans += min_cost * dist[i]

print(ans)