# 모든 명함을 수납할 수 있는 가장 작은 지갑을 만들 때, 지갑의 크기

def solution(sizes):
    a, b = 0, 0
    for s in sizes:
        if s[0] >= s[1]:
            a = max(a, s[0])
            b = max(b, s[1])
        else:
            a = max(a, s[1])
            b = max(b, s[0])
    
    return a * b