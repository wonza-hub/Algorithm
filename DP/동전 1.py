import sys
input=sys.stdin.readline

def sol():
	d=[0]*(k+1)
	d[0]=1
	
	for coin in coins:
		for j in range(coin,k+1):
			d[j]+=d[j-coin]

	return d[k]

n,k=map(int,input().rstrip().split())
coins=[int(input().rstrip()) for _ in range(n)]
coins.sort()
ans=sol()
print(ans)