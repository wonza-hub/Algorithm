def solution(n, times):
    answer = 0
    s, e = 0, max(times) * n
    while s <= e:
        m = (s + e) // 2
        cnt = 0
        for time in times:
            cnt += m // time
            if cnt >= n:
                break
                
        if cnt >= n:
            answer = m
            e = m - 1
        else:
            s = m + 1
            
    return answer

# 복습
def solution(n, times):
    s,e=0,int(1e13)
    ans=0
    while s<=e:
        m=(s+e)//2
        k=sum([m//t for t in times])
        if k<n:
            s=m+1
        else:
            ans=m
            e=m-1
        
    return ans