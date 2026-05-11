def solution(cap, n, deliveries, pickups):
    ans=0
    deliveries = [0] + deliveries
    pickups = [0] + pickups
    d_end,p_end=n,n
    
    while True:
        # 배달해야 하는 가장 먼 지점 찾기
        while d_end>0 and deliveries[d_end]==0:
            d_end-=1
        # 수거해야 하는 가장 먼 지점 찾기
        while p_end>0 and pickups[p_end]==0:
            p_end-=1
        if d_end==0 and p_end==0:
            break
        ans+=max(d_end,p_end)*2
        
        # 배달
        remain=cap
        i=d_end
        while i>0 and remain>0:
            take=min(remain,deliveries[i])
            remain-=take
            deliveries[i]-=take
            i-=1
        remain=cap
        i=p_end
        # 수거
        while i>0 and remain>0:
            take=min(remain,pickups[i])
            remain-=take
            pickups[i]-=take
            i-=1
        
    return ans
    
    
