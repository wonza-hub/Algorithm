def dfs(len):
    if len == 1 or len==2:
        return len
    else:
        dy[len] = dfs(len - 1) + dfs(len - 2)
        return dy[len]
    
n = int(input())
dy = [0] * (n + 1)
print(dfs(n))