import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    
    for operation in operations:
        op, v = operation.split(' ')
        if op == 'I':
            v = int(v)
            heapq.heappush(min_heap, v)
            heapq.heappush(max_heap, (v * -1, v))
            
        if op == "D":
            if len(min_heap) == 0:
                continue
            if v == "1":
                max_v = heapq.heappop(max_heap)[1]
                min_heap.remove(max_v)
            elif v == "-1":
                min_v = heapq.heappop(min_heap)
                max_heap.remove((min_v * -1, min_v))
    if min_heap:
        return [heapq.heappop(max_heap)[1], heapq.heappop(min_heap)]
    else:
        return [0,0]