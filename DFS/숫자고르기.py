from collections import defaultdict
import sys      
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(u, visit):
    visit.add(u)
    ch[u] = 1
    for v in g[u]:
        if v in visit:
            ans.extend(list(visit))
            return
        dfs(v, visit.copy())
        
n = int(input())
ch = [0] * (n + 1)
g = defaultdict(list)
for i in range(1, n + 1):
    v = int(input())
    g[v].append(i)

ans = []
for i in range(1, n + 1):
    if not ch[i]:
        dfs(i, set([]))

ans.sort()
print(len(ans))
for a in ans:
    print(a)