def solution(n, money):
    d=[1]+[0]*n
    money.sort()
    
    for m in money:
        for i in range(m,n+1):
            d[i]+=d[i-m]%1000000007
        
    return d[n]

# 복습 풀이
def solution(n, money):
    dp=[1]+[0]*n
    money.sort()
    
    for m in money:
        for i in range(m,n+1):
            dp[i]+=dp[i-m]%1_000_000_007
    
    return dp[n]