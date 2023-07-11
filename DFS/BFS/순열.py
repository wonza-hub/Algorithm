n, m = map(int, input().split())
result = [0] * m
check = [0] * (n + 1)
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
            if check[i] == 1:
                continue
            result[l] = i
            check[i] = 1
            dfs(l + 1)
            check[i] = 0
dfs(0)
print(cnt)