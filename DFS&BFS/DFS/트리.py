def dfs(delete_idx, nodes):
    nodes[delete_idx] = -2
    for i in range(len(nodes)):
        if nodes[i] == delete_idx:
            nodes[i] = -2
            dfs(i, nodes)

n = int(input())
nodes = list(map(int, input().split()))
delete_idx = int(input())
dfs(delete_idx, nodes)

ans = 0

for j in range(len(nodes)):
    if nodes[j] != -2 and j not in nodes:
        ans += 1
        
print(ans)