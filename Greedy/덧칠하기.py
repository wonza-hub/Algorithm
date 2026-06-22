def solution(n, m, section):
    answer = 0
    ch=[0]*(n+1)
    for s in section:
        if ch[s]:
            continue
        for i in range(s,s+m):
            if i>n:
                break
            ch[i]=1
        answer+=1
            
    return answer

# 다른 사람의 풀이
def solution(n, m, section):
    n = 0
    k = 0
    for s in section:
        if s > k:
            n += 1
            k = s+m-1
    return n