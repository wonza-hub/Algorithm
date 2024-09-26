def solution(arr):
    answer = [-1]
    for a in arr:
        if answer[-1] == a:
            continue
        answer.append(a)
    
    return answer[1:]

# 다른 사람의 풀이
def solution(arr):
    answer = []
    for a in arr:
        if len(answer) == 0 or answer[-1] != a:
            answer.append(a)
    
    return answer