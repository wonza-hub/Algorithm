# AI 풀이 참고
def solution(cost, hint):
    n=len(cost)
    memo={}
    
    # top-down 형식의 DP
    # 매 스테이지마다 번들을 사거나 안 사는 이분법 사고를 해야 함
    # bottom-up 보다 더 직관적으로 작성할 수 있을 것이라 판단
    def dp(stage,hints):
        if stage==n:
            return 0
        
        key=(stage,hints)
        if key in memo:
            return memo[key]
        
        # 힌트권을 n개 이상 가지고 있을 수도 있음
        # (같은 번호의 힌트권이 여러 장 포함될 수도 있습니다.)
        사용할수있는힌트권개수=min(hints[stage],n-1) 
        스테이지비용=cost[stage][사용할수있는힌트권개수]
        
        들고있는힌트권개수=list(hints)
        들고있는힌트권개수[stage]=0
        
        # 선택 1: 번들 안 삼
        res=스테이지비용+dp(stage+1,tuple(들고있는힌트권개수))
        # 선택 2: 번들 삼
        if stage<n-1:
            번들비용=hint[stage][0]
            new_hints=들고있는힌트권개수[:]
            for h in hint[stage][1:]:
                new_hints[h-1]+=1
            res=min(res,스테이지비용+번들비용+dp(stage+1,tuple(new_hints)))
            
        memo[key]=res
        return res
    
    return dp(0,tuple([0]*n))