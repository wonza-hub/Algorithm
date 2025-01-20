def solution(a,b,c):
  if b==1:
    return a%c
  tmp=solution(a,b//2,c)
  tmp=tmp*tmp%c
  if b%2==0:
    return tmp
  return tmp*a%c
  
a,b,c=map(int,input().split())
ans=solution(a,b,c)
print(ans)
