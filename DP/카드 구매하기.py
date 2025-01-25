n=int(input())
d=[0]+list(map(int,input().split()))

for i in range(1,n+1):
    for j in range(1,i//2+1):
        d[i]=max(d[i],d[j]+d[i-j])

print(d[n])