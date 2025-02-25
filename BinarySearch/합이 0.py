from bisect import bisect_left,bisect_right
import sys
input=sys.stdin.readline

n=int(input().rstrip())
arr=list(map(int,input().rstrip().split()))
arr.sort()
ans=0

def bs(s,e,t):
    global ans
    while s<e:
        sum=arr[s]+arr[e]

        if sum<t:
            s+=1
        elif sum>t:
            e-=1
        else:
            if arr[s]==arr[e]:
                ans+=(e-s+1)*(e-s)//2
                break
            else:
                bl=bisect_left(arr,arr[e])
                br=bisect_right(arr,arr[s])
                ans+=(br-s)*(e-(bl-1))
                s,e=br,bl-1


for i in range(n-2):
    s,e=i+1,n-1
    t=-arr[i]
    bs(s,e,t)

print(ans)