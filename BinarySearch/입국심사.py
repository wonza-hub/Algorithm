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