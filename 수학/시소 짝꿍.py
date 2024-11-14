from collections import Counter

def solution(weights):
    answer = 0
    c=Counter(weights)
    for k,v in c.items():
        if v>1:
            answer+=v*(v-1)//2
    weights=set(weights)
    for w in weights:
        if w*3/2 in weights:
            answer+=c[w]*c[w*3/2]
        if w*4/2 in weights:
            answer+=c[w]*c[w*4/2]
        if w*4/3 in weights:
            answer+=c[w]*c[w*4/3]

    return answer