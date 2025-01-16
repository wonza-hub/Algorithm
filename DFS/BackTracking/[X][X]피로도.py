# method1) 순열 라이브러리 사용
from itertools import permutations

def solution(k, dungeons):
    dun_cnts = []
    for perm in permutations(dungeons, len(dungeons)):
        cur_k = k
        dun_cnt = 0
        for p in perm:
            need_k, use_k = p
            if cur_k >= need_k:
                dun_cnt += 1
                cur_k -= use_k
        dun_cnts.append(dun_cnt)
    
    return max(dun_cnts)

# method2) 백트래킹 사용
answer = 0

def dfs(k, cnt, dungeons, ch):
    global answer
    answer = max(answer, cnt)
    for i in range(len(dungeons)):
        if k >= dungeons[i][0] and not ch[i]:
            ch[i] = 1
            dfs(k - dungeons[i][1], cnt + 1, dungeons, ch)
            ch[i] = 0
            
def solution(k, dungeons):
    ch = [0] * len(dungeons)
    dfs(k, 0, dungeons, ch)
    
    return answer

# 복습 풀이
# 일정 피로도를 사용해서 던전을 탐험할 수 있습니다
#
# 유저가 탐험할수 있는 최대 던전 수
#
# 유저의 현재 피로도 k
# "최소 필요 피로도"는 해당 던전을 탐험하기 위해 가지고 있어야 하는 최소한의 피로도
# "소모 피로도"는 던전을 탐험한 후 소모되는 피로도
# dungeons ["최소 필요 피로도", "소모 피로도"]/세로(행) 길이(즉, 던전의 개수)는 1 이상 8 이하
# 서로 다른 던전의 ["최소 필요 피로도", "소모 피로도"]가 서로 같을 수 있습니다.
from itertools import permutations

def solution(k, dungeons):
    answer = -1
    for per in permutations(dungeons, len(dungeons)):
        hp = k
        cnt = 0
        for p in per:
            m_hp, use_hp = p[0], p[1]
            if hp < m_hp:
                break
            cnt += 1
            hp -= use_hp
        answer = max(answer, cnt)
    
    
    return answer