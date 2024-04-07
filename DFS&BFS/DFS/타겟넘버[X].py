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
