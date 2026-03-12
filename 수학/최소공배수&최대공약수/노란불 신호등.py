import math
from functools import reduce

def lcm(a, b):
    return abs(a*b)//math.gcd(a,b)

def lcm_list(numbers):
    return reduce(lcm, numbers)

def solution(signals):
    answer = 0
    주기s=[]
    for 초,노,빨 in signals:
        주기=초+노+빨
        주기s.append(주기)
    최소공통주기=lcm_list(주기s)

    노란불켜지는시간=[[0]*(최소공통주기+1) for _ in range(len(signals))]
    
    for i,sig in enumerate(signals):
        초,노,빨=sig
        주기=주기s[i]
        k=0
        while True:
            s=초+1+주기*k
            e=초+노+주기*k
            if 최소공통주기<s:
                break
            for j in range(s,e+1):
                노란불켜지는시간[i][j]=1
            k+=1

    for 시각 in range(1,최소공통주기+1):
        cnt=0
        신호등갯수=len(signals)
        for sig in range(신호등갯수):
            if 노란불켜지는시간[sig][시각]==1:
                cnt+=1
        if cnt==신호등갯수:
            answer=시각
            break
    else:
        answer=-1
        
    return answer

# 다른 사람 풀이 참고: 나머지 활용
import math
from functools import reduce

def lcm(a,b):
    return abs(a*b)//math.gcd(a,b)

def lcm_list(numbers):
    return reduce(lcm,numbers)

def solution(signals):
    answer = 0
    주기s=[초+노+빨 for 초,노,빨 in signals]
    최소공통주기=lcm_list(주기s)

    for 시각 in range(1, 최소공통주기+1):
        모두노란불=True

        for 초,노,빨 in signals:
            주기=초+노+빨
            mod=시각%주기 # 나머지로 판단

            if not (초<=mod<=초+노-1):
                모두노란불=False
                break
                
        if 모두노란불:
            return 시각+1
    
    return -1