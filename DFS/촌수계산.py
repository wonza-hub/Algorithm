n = int(input())
s, e = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
flag = False

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(person, cnt):
    global flag
    visited[person] = True
    if person == e:
        flag = True
        print(cnt)
    for parent_or_child in graph[person]:
        if not visited[parent_or_child]:
            dfs(parent_or_child, cnt + 1)
            
dfs(s, 0)
if flag == False:
    print(-1)
