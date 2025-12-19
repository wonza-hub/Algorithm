import sys
input=sys.stdin.readline

n,m=map(int,input().split())
r,c,d=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def sol(x,y,d):
	ans=0
	while True:
		# 1. 현재 칸 청소
		arr[x][y]=2
		ans+=1
		# 2. 현재 칸 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
		flag=1
		while flag==1:
			for nd in ((d+3)%4,(d+2)%4,(d+1)%4,d):
				nx=x+dx[nd]
				ny=y+dy[nd]
				if arr[nx][ny]==0:
					x,y,d=nx,ny,nd
					flag=0
					break
			# 네 방향 모두 청소
			else:
				# 방향 유지한 채로 후진
				# 후진 시 벽이면 작동 중지
				nx=x-dx[d]
				ny=y-dy[d]
				if arr[nx][ny]==1:
					return ans
				else:
					x,y=nx,ny
	return -1
					
ans=sol(r,c,d)
print(ans)
		