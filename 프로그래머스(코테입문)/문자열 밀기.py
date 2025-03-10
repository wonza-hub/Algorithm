def solution(A, B):
    A*=2
    s,e=(len(A)-1)//2+1,len(A)-1
    ans=0
    while s>0:
        if A[s:e+1]==B:
            break
        ans+=1
        s-=1
        e-=1
    else:
        ans=-1
        
    return ans