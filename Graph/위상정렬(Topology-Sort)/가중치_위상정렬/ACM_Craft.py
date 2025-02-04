from collections import deque
import sys
input = sys.stdin.readline
import copy

def topology_sort(target):
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            result[i] = time[i]

    while q:
        now = q.popleft()
        if now == target:
            print(result[now])
            return
        result.append(now)
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
    target = int(input()) 

    topology_sort(target)