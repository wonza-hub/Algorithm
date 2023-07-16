t = int(input())
k = int(input())
p = [0] * k
n = [0] * k
cnt = 0
for i in range(k):
    p[i], n[i] = map(int, input().split())

def dfs(l, sum):
    global cnt
    if sum > t:
        return
    if l == k:
        if sum == t:
            cnt += 1
    else:
        for i in range(n[l] + 1):
            dfs(l + 1, sum + p[l] * i)
        
dfs(0, 0)
print(cnt)

            