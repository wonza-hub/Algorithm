n=int(input())
d=[0]*(n+1)
r=[0]*(n+1)
d[1],r[1]=0,0

for i in range(2,n+1):
    cnt=1e9
    if i%2==0:
       if cnt>d[i//2]+1:
          r[i]=i//2
          cnt=d[i//2]+1
    if i%3==0:
       if cnt>d[i//3]+1:
          r[i]=i//3
          cnt=d[i//3]+1
    if cnt>d[i-1]+1:
        r[i]=i-1
        cnt=d[i-1]+1
    d[i]=cnt

print(d[n])
idx=n
while True:
   if idx==0:
      break
   print(idx,end=" ")
   idx=r[idx]