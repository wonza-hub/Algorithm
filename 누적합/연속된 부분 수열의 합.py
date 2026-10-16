def solution(sequence, k):
    s,e=0,0
    max_len=1_000_001
    ans=[0,1_000_000]
    N=len(sequence)
    부분수열합=sequence[0]
    
    while True:
        length=e-s+1
        
        if 부분수열합<=k:
            if 부분수열합==k:
                if length<max_len:
                    max_len=length
                    ans=[s,e]
            e+=1
            if e>=N:
                break
            부분수열합+=sequence[e]
        else:
            부분수열합-=sequence[s]
            s+=1
    return ans