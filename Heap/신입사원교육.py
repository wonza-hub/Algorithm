import heapq as hq

def solution(ability, number):
    hq.heapify(ability)
    while number > 0:
        a = hq.heappop(ability)
        b = hq.heappop(ability)
        a, b = a + b, a + b
        hq.heappush(ability, a)
        hq.heappush(ability, b)
        number -= 1
    
    return sum(ability)