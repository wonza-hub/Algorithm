import sys
input=sys.stdin.readline

n,m=map(int,input().rstrip().split())
arr=[list(map(int,input().rstrip().split())) for _ in range(n)]

ans=0
for i in range(n):
	for j in range(m):
		# 범위경계 및 경계 포함여부 유의
        # 끝 경계 유의
		if j<m-3:
			# 1X4
			원포=arr[i][j:j+4]
			ans=max(ans,sum(원포))
		if i<n-3:
			# 4X1
			포원=[arr[i+k][j] for k in range(4)]
			ans=max(ans,sum(포원))
		if i<n-1 and j<m-1:
			# 2X2
			투투=arr[i][j:j+2]+arr[i+1][j:j+2]
			ans=max(ans,sum(투투))
		if i<n-2 and j<m-1:
			# 3X2
			쓰리투=투투+arr[i+2][j:j+2]
			tmp=[쓰리투[x-1]+쓰리투[y-1] for x,y in [(2,4),(1,3),(4,6),(3,5),(2,5),(1,6),(1,5),(2,6)]]
			최대=sum(쓰리투)-min(tmp)
			ans=max(ans,최대)
		if i<n-1 and j<m-2:
			# 2X3
			투쓰리=arr[i][j:j+3]+arr[i+1][j:j+3]
			tmp=[투쓰리[x-1]+투쓰리[y-1] for x,y in [(5,6),(1,2),(2,3),(4,5),(1,6),(3,4),(4,6),(1,3)]]
			최대=sum(투쓰리)-min(tmp)
			ans=max(ans,최대)
			
print(ans)