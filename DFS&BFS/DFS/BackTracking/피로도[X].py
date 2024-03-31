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
            