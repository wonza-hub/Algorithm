from collections import deque 

def solution(bridge_length, weight, truck_weights):
    truck_weights=deque(truck_weights)
    cur_time,cur_weight=0,0
    bridge=deque([])
    
    while len(bridge)>0 or len(truck_weights)>0:
        # 통과 가능 여부 검사
        if len(bridge)>0:
            time=bridge[0][1]
            if cur_time-time==bridge_length:
                w,_=bridge.popleft() # 통과
                cur_weight-=w
        # 입장 가능 여부 검사
        # - 다리가 꽉 차지 않음
        # - 다리 무게가 무게 한도보다 가벼움
        if len(bridge)!=bridge_length and len(truck_weights)>0 and cur_weight+truck_weights[0]<=weight:
            tw=truck_weights.popleft()
            bridge.append((tw,cur_time))
            cur_weight+=tw
        cur_time+=1
        
    return cur_time