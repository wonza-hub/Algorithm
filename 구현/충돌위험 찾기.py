from collections import Counter

def 경로저장(로봇번호,sa,sb,ea,eb,로봇경로):
    sx,ex,sy,ey=sa,ea,sb,eb
    # 시작점 중복 방지
    if not (len(로봇경로[로봇번호])!=0 and sa==로봇경로[로봇번호][-1][0] and sb==로봇경로[로봇번호][-1][1]):
        로봇경로[로봇번호].append((sx,sy))
    while sx!=ex:
        if sx<ex:
            sx+=1
        elif sx>ex:
            sx-=1
        로봇경로[로봇번호].append((sx,sy))
    while sy!=ey:
        if sy<ey:
            sy+=1
        elif sy>ey:
            sy-=1
        로봇경로[로봇번호].append((sx,sy))
    
def solution(points, routes):
    points=[0]+points
    answer = 0
    로봇경로=[[] for _ in range(len(routes))]
    for i in range(len(routes)): 
        for j in range(len(routes[i])-1):
            sa,sb=points[routes[i][j]]
            ea,eb=points[routes[i][j+1]]
            경로저장(i,sa,sb,ea,eb,로봇경로)
            
    maxr=max(len(r) for r in 로봇경로)
    for time in range(maxr):
        counter=Counter()
        for j in range(len(로봇경로)):
            if len(로봇경로[j])-1<time:
                continue
            counter[로봇경로[j][time]]+=1
        # 중요 포인트
        answer+=sum(1 for v in counter.values() if v>=2)
            
    return answer