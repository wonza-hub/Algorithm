ans=1
n=int(input())
m=int(input())
pt=[]
d=[0]*41
d[1],d[2]=1,2
for i in range(3,n+1):
    d[i]=d[i-1]+d[i-2]
for _ in range(m):
    pt.append(int(input()))
pt.append(n+1)

tmp=0
for p in pt:
    if p-tmp-1>0:
        ans*=d[p-tmp-1]
    tmp=p
print(ans)

