from collections import deque

N, K = map(int, input().split())

graph = []
data = []

for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(N):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))

data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

while q:
    virus, s, x, y = q.popleft()
    if s == target_s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx and nx < N and 0 <= ny and ny < N:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))
                
print(graph[target_x - 1][target_y - 1])

# 복습 풀이
import sys
input=sys.stdin.readline
from collections import deque

dx=[-1,0,1,0]
dy=[0,1,0,-1]

n,k=map(int,input().split())
arr=[[0]*(n+1)]+[[0]+list(map(int,input().split())) for _ in range(n)]
s,x,y=map(int,input().split())

def bfs():
	while q:
		v,x,y,t=q.popleft()
		if t==s:
			break
		for i in range(4):
			nx=x+dx[i]
			ny=y+dy[i]
			if nx<=0 or nx>n or ny<=0 or ny>n or arr[nx][ny]!=0:
				continue
			arr[nx][ny]=v
			q.append((v,nx,ny,t+1))

tmp=[]
for i in range(1,n+1):
	for j in range(1,n+1):
		if arr[i][j]==0:
			continue
		tmp.append((arr[i][j],i,j,0))
tmp.sort(key=lambda x:x[0])
q=deque(tmp)

bfs()
print(arr[x][y] if arr[x][y]!=0 else 0)


        