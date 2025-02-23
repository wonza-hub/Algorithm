# INF = int(1e9)
# n = int(input())
# dis = [[INF] * (n + 1) for _ in range(n + 1)]
# arr = [0] * (n + 1)
# for i in range(1, n + 1):
#     dis[i][i] = 0
            
# while True:
#     a, b = map(int, input().split())
#     if a == -1 and b == -1:
#         break
#     dis[a][b] = 1
#     dis[b][a] = 1

# for k in range(1, n + 1):
#     for a in range(1, n + 1):
#         for b in range(1, n + 1):
#             dis[a][b] = min(dis[a][b], dis[a][k] + dis[k][b])

# score = 100
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         arr[i] = max(arr[i], dis[i][j])
#     score = min(score, arr[i])

# cnt = arr.count(score)
# print(score, cnt)
# for i in range(1, n + 1):
#     if arr[i] == score:
#         print(i, end = " ")

# 복습 풀이
import sys
input=sys.stdin.readline

n=int(input().rstrip())
INF=50
graph=[[INF]*(n+1) for _ in range(n+1)]
score=[0]*(n+1)

while True:
    a,b=map(int,input().rstrip().split())
    if a==-1 and b==-1:
        break
    graph[a][b]=1
    graph[b][a]=1

for i in range(1,n+1):
    graph[i][i]=1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

min_score=50
for s in range(1,n+1):
    max_score=max(graph[s][1:])
    score[s]=max_score
    min_score=min(min_score,max_score)

print(min_score,score.count(min_score))
for t in range(1,n+1):
    if score[t]==min_score:
        print(t,end=" ")