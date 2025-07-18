import sys
input=sys.stdin.readline

n=int(input().rstrip())
target=list(input().rstrip())
ans=0

for _ in range(n-1):
    cmp=list(input().rstrip())
    tar=target[:]
    rem=0

    for w in cmp:
        if w in tar:
            tar.remove(w)
        else:
            rem+=1
    
    if rem<=1 and len(tar)<=1:
        ans+=1

print(ans)