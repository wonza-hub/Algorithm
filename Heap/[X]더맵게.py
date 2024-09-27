import heapq as hq
    
def solution(scoville, K):
    answer = 0
    hq.heapify(scoville)
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            if first < K:
                answer = -1
                break
            else:
                break
        second = hq.heappop(scoville)
        new = first + second * 2
        hq.heappush(scoville, new)
        answer += 1
        
    return answer

# 복습 풀이
import heapq as hq

def solution(scoville, K):
    hq.heapify(scoville)
    answer = 0
    while len(scoville) > 1 and scoville[0] < K:
        answer += 1
        a = hq.heappop(scoville)
        b = hq.heappop(scoville)
        c = a + 2 * b
        hq.heappush(scoville, c)
    if scoville[0] < K:
        answer = -1
    
    return answer