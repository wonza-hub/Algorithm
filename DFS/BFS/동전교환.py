n = int(input())
coins = list(map(int, input().split()))
coins.sort(reverse=True)
m = int(input())
answer = 10e9


def dfs(l, sum):
    global answer, min_lev
    if l >= answer:
        return
    if sum > m:
        return
    if sum == m:
        answer = min(l, answer)
    else:
        for i in range(n):
            dfs(l + 1, sum + coins[i])


dfs(0, 0)
print(answer)