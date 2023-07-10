n = int(input())
arr = list(map(int, input().split()))
total = sum(arr)

def dfs(L, sum):
    if sum > total//2:
        return
    if L == n: 
        if sum == (total - sum):
            print("YES")
            return
        else:
            print("NO")
            return
    else:
        dfs(L + 1, sum + arr[L])
        dfs(L + 1, sum)

dfs(0, 0)