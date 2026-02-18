from collections import defaultdict

def solution(survey, choices):
    answer = ''
    dic=defaultdict(int)
    score=[0,3,2,1,0,1,2,3]
    
    for sur,ch in zip(survey,choices):
        da,a=sur[0],sur[1]
        if ch in [1,2,3]:
            dic[da]+=score[ch]
        elif ch in [5,6,7]:
            dic[a]+=score[ch]
        else:
            continue

    # 각 지표는 이미 사전순임    
    for 지표1,지표2 in [['R','T'],['C','F'],['J','M'],['A','N']]:
        if dic[지표1]>=dic[지표2]:
            answer+=지표1
        elif dic[지표1]<dic[지표2]:
            answer+=지표2
            
    return answer