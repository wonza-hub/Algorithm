from collections import Counter

def solution(array):
    if len(set(array))==1: # [1], [1, 1] 과 같은 경우 처리
        return array[0]
    
    a=Counter(array).most_common(2)
    print(a)
    
    return -1 if a[0][1]==a[1][1] else a[0][0] 