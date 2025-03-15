def solution(A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)
    ans,i,j=0,0,0
    while i<len(A):
        if A[i]<B[j]:
            ans+=1
            j+=1
        i+=1
    
    return ans