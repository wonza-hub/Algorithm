ans = 0

def dfs(l, um, ability, visit):
    global ans
    n = len(ability)        # 학생 수
    m = len(ability[0])     # 종목 개수
    
    # 종목별로 대표가 다 정해졌으면
    if l == m:
        ans = max(ans, sum)   # 능력치 합의 최댓값을 갱신
        
        return
    for i in range(n):
        if visit[i] == 0:
            visit[i] = 1
            dfs(l + 1, sum + ability[i][l], ability, visit)
            visit[i] = 0

# Permutations 풀이
from itertools import permutations

def solution(ability):
    answer = 0
    
    nPr = list(permutations(ability, len(ability[0])))
    
    for i in range(len(nPr)):
        total = 0
        for j in range(len(nPr[i])):
            total += nPr[i][j][j]
        answer = max(answer, total)
    
    return answer
