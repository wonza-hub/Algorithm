n=int(input())
lope=[]

for _ in range(n):
    lope.append(int(input()))

lope.sort()
l=len(lope)
ans=lope[0]
for i in range(l):
    ans=max(ans,lope[i]*(l-i))

print(ans)