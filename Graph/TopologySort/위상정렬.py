# * 정석 풀이
from collections import deque

# 노드 개수, 간선 개수 입력
v, e = map(int, input().split())
# 모든 노드에 대한 진입차수 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결리스트 초기화
graph = [[] for i in range(v + 1)]

# 방향 그래프의 모든 간선 정보를 입력
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = [] # 알고리즘 수행 결과
    q = deque()

    # 최초과정: 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    # 이후 큐가 빌 때까지 반복
    while q:
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 차감
        # 차감 이후 진입차수가 0이 됐다면 해당 노드를 큐에 삽입
        if indegree[i] == 0:
            q.append(i)


# * 간선 정보를 2차원으로 표현
from collections import deque

n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
indegree = [0] * (n + 1)

q = deque()

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    indegree[b] += 1

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    x = q.popleft()
    print(x, end = " ")
    for i in range(1, n + 1):
        if graph[x][i] == 1:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)