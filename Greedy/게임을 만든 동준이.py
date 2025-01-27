n=int(input())
arr=[]
for _ in range(n):
    arr.append(int(input()))
arr.reverse()
ans=0
for i in range(1,n):
    if arr[i]>=arr[i-1]:
        tmp=arr[i-1]-1
        de=arr[i]-tmp
        arr[i]=tmp
        ans+=de

print(ans)