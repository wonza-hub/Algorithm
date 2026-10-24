from collections import defaultdict

def solution(skill, skill_trees):
    ans=0
    dic=defaultdict(int)
    
    for i in range(len(skill)):
        dic[skill[i]]=i
        
    for tree in skill_trees:
        cur=0
        for skill in tree:
            if skill not in dic:
                continue
            
            if dic[skill]!=cur:
                break
            cur+=1
        else:
            ans+=1
            
    return ans

# 다른 사람의 풀이 (스택/큐를 활용한 풀이)
def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer