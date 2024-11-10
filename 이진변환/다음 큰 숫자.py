def solution(n):
    answer = 0
    ncnt=list(bin(n)[2:]).count('1')
    nn=n+1
    while True:
        nncnt=list(bin(nn)[2:]).count('1')
        if nncnt==ncnt:
            answer=nn
            break
        nn+=1
        
    return answer