import sys
input=sys.stdin.readline

n,k=map(int,input().rstrip().split())
d=[[0]*(n+1) for _ in range(k+1)]
d[1]=[1]*(n+1)

# N=6, K=4 일 때, (4,6)이 되는 경우는
# (1,6)+(3,0), (1,5)+(3,1), ..., (1,0)+(3,6) 과 같다.
# 여기서 (1,6)+(3,0)를 보면, (3,0)이 되는 경우는 (1,0)+(2,0),
# (1,0)+(3,6)를 보면, (3,6)이 되는 경우는 (1,6)+(2,0), (1,5)+(2,1), ...
# 이와 같은 논리로 진행하면 dp로 이전 행의 결과를 활용하여 답을 도출할 수 있다.
for i in range(2,k+1):
    for j in range(n+1):
        if j==0:
            d[i][j]=1
            continue
        for s in range(j+1):
            d[i][j]+=d[i-1][s]

print(d[k][n]%1000000000)