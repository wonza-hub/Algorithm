import heapq as hq

def solution(n, k, enemy):
    if k >= len(enemy):
        return len(enemy)
    answer = 0
    num = 0
    heap = []
    
    for e in enemy:
        # 최대힙
        hq.heappush(heap, -e)
        num += e
        if num > n:
            if not k:
                break
            # 이전 적군 무효화
            k -= 1
            num += hq.heappop(heap)
        answer += 1
    
    return answer