n = int(input())
result = [0] * n
check = [0] * (n + 1)

def dfs(idx):
    if idx == n:
        for j in range(n):
            print(result[j], end=" ")
        print()
    else:
        for i in range(1, n + 1):
            if check[i] == 1:
                continue
            result[idx] = i
            check[i] = 1
            dfs(idx + 1)
            check[i] = 0

dfs(0)
