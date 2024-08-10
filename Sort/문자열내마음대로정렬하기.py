def solution(strings, n):
    # 람다 표현식 정렬 기준 두 개 이상
    strings.sort(key = lambda x: (x[n], x))
    
    return strings