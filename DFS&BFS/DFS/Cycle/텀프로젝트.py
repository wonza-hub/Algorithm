def dfs(x):
    global ans
    ch[x] = 1
    cycle.append(x)
    pick = picks[x]

    if ch[pick]:
        if pick in cycle:
            ans += cycle[cycle.index(pick):]
    else:
        dfs(pick)

t = int(input())
for _ in range(t):
    n = int(input())
    picks = [0] + list(map(int, input().split()))
    ch = [1] + [0] * n
    ans = []
    
    for i in range(1, n + 1):
        if not ch[i]:
            cycle = []
            dfs(i)
            
    print(n - len(ans))