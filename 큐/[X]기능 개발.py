def solution(progresses, speeds):
    answer = []
    while progresses:
        cnt = 0
        while progresses and progresses[0] >= 100:
            cnt+=1
            progresses.pop(0)
            speeds.pop(0)
        progresses = [progresses[i] + speeds[i] for i in range(len(progresses))]
        if cnt:
            answer.append(cnt)
    
    return answer

# 복습 풀이
from collections import deque

def solution(progresses, speeds):
    ans=[]
    progresses=deque(progresses)
    speeds=deque(speeds)

    while progresses:
        cnt=0
        while progresses and progresses[0]==100:
            cnt+=1
            progresses.popleft()
            speeds.popleft()
        progresses=deque([min(100,progresses[i]+speeds[i]) for i in range(len(progresses))])
        if cnt:
            ans.append(cnt)
        
    return ans
        
                