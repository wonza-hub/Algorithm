def solution(num, total):
    s=(total-sum([i for i in range(1,num)]))//num
    
    return [n for n in range(s,s+num)]