import sys
input=sys.stdin.readline

n,s,m=map(int,input().rstrip().split())
v=[0]+list(map(int,input().rstrip().split()))

d=[[0]*(m+1) for _ in range(n+1)]
d[0][s]=1

for i in range(1,n+1):
    for j in range(m+1):
        # 이전 곡에서 볼륨이 j인 경우
        if d[i-1][j]:
            # 볼륨을 높이거나 낮췄을 경우, 범위 내에 있으면 현재 곡의 dp에 저장
            if j+v[i]<=m:
                d[i][j+v[i]]=1
            if j-v[i]>=0:
                d[i][j-v[i]]=1

# 마지막 곡에 대해 높은 볼륨부터 역순으로 탐색
for k in range(m,-1,-1):
    if d[n][k]:
        print(k)
        break
# 마지막 곡을 연주할 수 없는 경우
else:
    print(-1)