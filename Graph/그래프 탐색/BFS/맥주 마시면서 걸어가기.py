import sys
input=sys.stdin.readline
from collections import deque

def sol(graph):
	q=deque()
	q.append([0,20])
	ch=[0]*(n+2)
	while q:
		s,beer=q.popleft()
		ch[s]=1
		if beer<=0:
			break
		# 목적지에 도달했는지 확인
		if s==len(graph)-1:
			return True
		for e,d in graph[s]:
            # 이미 방문한 곳이면 패스
			if ch[e]==1:
				continue
			# 거리가 맥주 20병으로 갈 수 있는 거리(50m*20)보다 멀면 패스
			if d>beer*50:
				continue
			q.append([e,20])
	return False
	
for _ in range(int(input())):
	n=int(input())
	vtx=[]
	graph=[[] for _ in range(n+2)]
	hx,hy=map(int,input().split())
	vtx.append((hx,hy))
	for _ in range(n):
		px,py=map(int,input().split())
		vtx.append((px,py))
	fx,fy=map(int,input().split())
	vtx.append((fx,fy))
	for i in range(n+2):
		for j in range(n+2):
			if i==j:
				continue 
			sx,sy=vtx[i]
			ex,ey=vtx[j]
			d=abs(sx-ex)+abs(sy-ey)
			graph[i].append([j,d])
	ans=sol(graph)
	print('happy' if ans==True else 'sad')
		
		