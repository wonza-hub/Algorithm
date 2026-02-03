n, m = map(int, input().split())
result = [0] * m
check = [0] * (n + 1)

def dfs(l):
    if l == m:
        for j in range(m):
            print(result[j], end=" ")
        print()
    else:
        for i in range(1, n + 1):
            if check[i] == 1:
                continue
            result[l] = i
            check[i] = 1
            dfs(l + 1)
            check[i] = 0
dfs(0)

# 복습 풀이
import sys
input=sys.stdin.readline

n,m=map(int,input().rstrip().split())
arr=[0]*m
ch=[0]*(n+1)

def dfs(l):
	if l==m:
		print(' '.join(map(str,arr)))
		return
	for i in range(1,n+1):
		if not ch[i]:
			arr[l]=i
			ch[i]=1
			dfs(l+1)
			ch[i]=0
			
dfs(0)
