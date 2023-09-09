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