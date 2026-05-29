# 풀이 참고
from itertools import combinations
from collections import defaultdict
import bisect

def solution(info, query):
    answer = []
    info=[i.split(' ') for i in info]
        
    table=defaultdict(list)
    for i in info:
        attrs=i[:4]
        score=int(i[4])
        
        # 한 지원자가 속할 수 있는 모든 조합 생성 (최대 4개 속성, 각 속성은 선택 또는 '-'로 대체)
        for r in range(5):
            for combo in combinations(range(4),r):
                key=attrs[:]
                for idx in combo:
                    key[idx]='-'
                key=tuple(key)
                table[key].append(score)
    
    # 점수 정렬 (이진 탐색을 위해)
    for v in table.values():
        v.sort()
        
    query=[q.split(' ') for q in query]
    for q in query:
        x=int(q[-1])
        key=tuple(q[::2])
        # 이진 탐색으로 점수 조건을 만족하는 지원자 수 계산
        cnt=len(table[key])-bisect.bisect_left(table[key],x)
        answer.append(cnt)
    
    return answer