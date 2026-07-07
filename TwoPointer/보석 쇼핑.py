# 풀이 참고
from collections import defaultdict

def solution(gems):
    need=len(set(gems))
    s=0
    cnt=0
    window=defaultdict(int)
    best=None
    
    for e in range(len(gems)):
        if window[gems[e]]==0:
            cnt+=1
        window[gems[e]]+=1
        
        # 모든 종류를 포함한다면, 좌포인터를 최대한 우측으로 옮김
        while cnt==need:
            if best is None or (e-s)<(best[1]-best[0]):
                best=(s,e)
            window[gems[s]]-=1
            if window[gems[s]]==0:
                cnt-=1
            s+=1
    return [best[0]+1,best[1]+1]
        