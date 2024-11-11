from collections import defaultdict

def solution(k, tangerine):
    answer=0
    int_dict=defaultdict(int)
    for t in tangerine:
        int_dict[t]+=1
    arr=list(int_dict.values())
    arr.sort(reverse=True)
    sum=0
    for qty in arr:
        sum+=qty
        answer+=1
        if sum>=k:
            break
    
    return answer