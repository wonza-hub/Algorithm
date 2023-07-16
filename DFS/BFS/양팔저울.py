k = int(input())
weights = list(map(int, input().split()))
sum_all = sum(weights)
result = set()

def dfs(l, sum):
    global result
    if l == k:
        if 0 < sum <= sum_all:
            result.add(sum)
    else:
        dfs(l + 1, sum + weights[l])
        dfs(l + 1, sum - weights[l])
        dfs(l + 1, sum)

dfs(0, 0)
print(sum_all - len(result))