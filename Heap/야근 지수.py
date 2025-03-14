import heapq as hq

def solution(n, works):
    # early return
    if sum(works)<n:
        return 0

    # 최대 힙으로 초기화
    hq.heapify(works:=[-w for w in works])
    while n:
        n-=1
        # 매번 작업량이 가장 많이 남은 작업부터 처리
        w=hq.heappop(works)
        # 남은 작업량이 양수인 경우는 작업을 끝낸다는 의미이므로, 0으로 저장
        hq.heappush(works,min(0,w+1))
        
    return sum([w**2 for w in works])