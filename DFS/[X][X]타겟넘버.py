def solution(numbers, target):
    answer= 0
    def dfs(i, sum):
        nonlocal answer
        if i==len(numbers):
            if sum==target:
                answer+= 1
        else:
            dfs(i+1, sum+numbers[i])
            dfs(i+1, sum-numbers[i])
    dfs(0,0)
    return answer

# dfs 함수 분리
def dfs(l, sum, numbers, target):
    global answer
    if l == len(numbers):
        if sum == target:
            answer += 1
            
        return         
        
    dfs(l + 1, sum + numbers[l], numbers, target)
    dfs(l + 1, sum - numbers[l], numbers, target)          

def solution(numbers, target):
    global answer
    answer = 0
    dfs(0, 0, numbers, target)
    
    return answer

# 복습 풀이
# 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다.
#
# 타겟 넘버를 만드는 방법의 수
def dfs(i, s, target, numbers):
    global answer
    if i == len(numbers):
        if s == target:
            answer += 1
        return
    
    dfs(i + 1, s + numbers[i], target, numbers)
    dfs(i + 1, s - numbers[i], target, numbers)
    
def solution(numbers, target):
    global answer
    answer = 0
    dfs(0, 0, target, numbers)
    
    return answer