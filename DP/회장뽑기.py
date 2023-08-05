INF = int(1e9)
n = int(input())
dis = [[INF] * (n + 1) for _ in range(n + 1)]
arr = [0] * (n + 1)
for i in range(1, n + 1):
    dis[i][i] = 0
            
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    dis[a][b] = 1
    dis[b][a] = 1

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            dis[a][b] = min(dis[a][b], dis[a][k] + dis[k][b])

score = 100
for i in range(1, n + 1):
    for j in range(1, n + 1):
        arr[i] = max(arr[i], dis[i][j])
    score = min(score, arr[i])

cnt = arr.count(score)
print(score, cnt)
for i in range(1, n + 1):
    if arr[i] == score:
        print(i, end = " ")