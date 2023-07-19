n, m = map(int, input().split())
result = [0] * m
cnt = 0

def dfs(l):
    global cnt
    if l == m:
        for j in range(m):
            print(result[j], end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, n + 1):
            result[l] = i
            dfs(l + 1)

dfs(0)
print(cnt)