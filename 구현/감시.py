import sys
input=sys.stdin.readline

dx=[-1,0,1,0]
dy=[0,1,0,-1]
cctv=[[],[1],[1,3],[0,1],[0,1,3],[0,1,2,3]]

def calc(tlst):
	global CCTV_CNT
	ch=[[0]*(m+2) for _ in range(n+2)]
	# 모든 CCTV에 대해 처리(좌표,type,rot)
	for i in range(CCTV_CNT):
		sx,sy=lst[i] # 1~n,1~m
		rot=tlst[i] # 0~3
		type=arr[sx][sy] # 1~5
		# type에 따라 모든 방향을 뻗어가면서 ch[] 1 표시 
		for dr in cctv[type]:
			dr=(dr+rot)%4
			cx,cy=sx,sy
			while True:
				cx=cx+dx[dr]
				cy=cy+dy[dr]
				if arr[cx][cy]==6:
					break
				ch[cx][cy]=1

	# 사각지대(빈칸 && 미방문) 개수 카운트
	cnt=0
	for i in range(1,n+1):
		for j in range(1,m+1):
			if arr[i][j]==0 and ch[i][j]==0:
				cnt+=1

	return cnt
		
			
def dfs(n,tlst):
	global ans
	if n==CCTV_CNT:
		ans=min(ans,calc(tlst)) # 모든 CCTV 방향(0~3) 정하기 완료
		return

	# 가능한 모든 방향 탐색
	dfs(n+1,tlst+[0]) # 0도 회전
	dfs(n+1,tlst+[1]) # 90도 회전
	dfs(n+1,tlst+[2]) # 180도 회전
	dfs(n+1,tlst+[3]) # 270도 회전
	
n,m=map(int,input().rstrip().split())
arr=[[6]*(m+2)]+[[6]+list(map(int,input().rstrip().split()))+[6] for _ in range(n)]+[[6]*(m+2)]

lst=[]
for i in range(1,n+1):
	for j in range(1,m+1):
		if 1<=arr[i][j]<=5:
			lst.append((i,j))

CCTV_CNT=len(lst)
ans=n*m
dfs(0,[])
print(ans)