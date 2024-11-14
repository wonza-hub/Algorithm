from collections import Counter

def solution(want, number, discount):
    answer = 0
    wants=dict(zip(want,number))
    
    for i in range(len(discount)-9):
        c=dict(Counter(discount[i:i+10]))
        if wants==c:
            answer+=1
    
    return answer