from collections import Counter
from itertools import combinations

def solution(orders, course):
    orders=[''.join(sorted(list(order))) for order in orders]
    answer = []
    for c in course:
        candis=[]
        for order in orders:
            for combi in combinations(order,c):
                candis.append(''.join(list(combi)))
        mc=Counter(candis).most_common()
        if len(mc)<1:
            continue
        tmp=mc[0][1]
        for order,cnt in mc:
            if cnt<2:
                break
            if cnt!=tmp:
                break
            answer.append(order)
            
    return sorted(answer)