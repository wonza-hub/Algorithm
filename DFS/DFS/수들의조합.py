n, k = map(int, input().split())
data = list(map(int, input().split()))
m = int(input())
cnt = 0

def dfs(l, s, sum):
    global cnt
    if l == k:
        if sum % m == 0:
            cnt += 1
        return
    else:
        for i in range(s, n):
            dfs(l + 1, i + 1, sum + data[i])

dfs(0, 0, 0)
print(cnt)