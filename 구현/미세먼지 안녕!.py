from copy import deepcopy
import sys
input=sys.stdin.readline

dx=[-1,0,1,0]
dy=[0,-1,0,1]

r,c,t=map(int,input().rstrip().split())
arr=[list(map(int,input().rstrip().split())) for _ in range(r)]
i1,i2=0,0
for i in range(r):
	if arr[i][0]==-1:
		# 공기청정기 위치 복사
		i1,i2=i,i+1
		# 공기청정기 위치 0으로 초기화
		arr[i1][0]=0
		arr[i2][0]=0
		break
		

def 확산(i,j,dust,tmp):
	확산량=int(dust/5)
	확산방향개수=0
	# 네 방향 확인
	for k in range(4):
		ni=i+dx[k]
		nj=j+dy[k]
		# 범위 밖
		if ni<0 or ni>=r or nj<0 or nj>=c:
			continue
		# 공기청정기
		if (ni==i1 and nj==0) or (ni==i2 and nj==0):
			continue
			
		확산방향개수+=1
		tmp[ni][nj]+=확산량
		
	남은량=dust-확산량*확산방향개수
	tmp[i][j]+=남은량
	

def 위순환(arr):
	# V
	for i in range(i1-1,0,-1):
		arr[i][0]=arr[i-1][0]
	# <
	for j in range(0,c-1):
		arr[0][j]=arr[0][j+1]
	# ^
	for i in range(0,i1):
		arr[i][c-1]=arr[i+1][c-1]
	# >
	for j in range(c-1,0,-1):
		arr[i1][j]=arr[i1][j-1]
		
def 아래순환(arr):
	# ^
	for i in range(i2+1,r-1):
		arr[i][0]=arr[i+1][0]
	# <
	for j in range(0,c-1):
		arr[r-1][j]=arr[r-1][j+1]
	# V
	for i in range(r-1,i2,-1):
		arr[i][c-1]=arr[i-1][c-1]
	# >
	for j in range(c-1,0,-1):
		arr[i2][j]=arr[i2][j-1]
	

for _ in range(t):
	tmp=[[0]*c for _ in range(r)]
	for i in range(r):
		for j in range(c):
			if arr[i][j]==-1:
				continue
			if arr[i][j]!=0:
				확산(i,j,arr[i][j],tmp)
	
	new_arr=deepcopy(tmp)
	위순환(new_arr)
	아래순환(new_arr)
	arr=new_arr

ans=sum([sum(a) for a in arr])
print(ans)
