n, m = map(int, input().split())
matrix = [[0] * (n + 1) for _ in range(n + 1)]
check = [0] * (n + 1)
cnt = 0

for _ in range(m):
    start, end = map(int, input().split())
    matrix[start][end] = 1


def dfs(start):
    global cnt
    if start == n:
        cnt += 1
        return
    for i in range(1, n + 1):
        if check[i] == 0 and matrix[start][i] == 1:
            check[i] = 1
            dfs(i)
            check[i] = 0


check[1] = 1
dfs(1)
print(cnt)
