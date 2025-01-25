n,m=map(int,input().split())
d=[list(map(int,input())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if d[i][j]==1:
            if i and j and d[i-1][j-1] and d[i-1][j] and d[i][j-1]:
                d[i][j]=min(d[i-1][j-1],d[i-1][j],d[i][j-1])+1
ml=0
for i in range(n):
    for j in range(m):
        ml=max(ml,d[i][j])

print(ml*ml)