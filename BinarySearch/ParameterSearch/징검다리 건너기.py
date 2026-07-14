def solution(stones, k):
    ans=0
    s=0;e=max(stones)

    while s<=e:
        m=(s+e)//2
        p=-1

        for i in range(len(stones)):
            # m번째 사람이 밟으면 정확히 0이 되어,
            # m명 모두 무사히 밟고 지나갈 수 있음
            if stones[i]>=m:
                tmp=p
                p=i
                if p-tmp>k:
                    e=m-1
                    break
        else:
            if len(stones)-p<=k:
                ans=m
                s=m+1
            else:
                e=m-1
                
    return ans