from collections import deque, defaultdict

def solution(begin, target, words):
    answer = 0
    ch = defaultdict(int)
    if target not in words:
        return 0
    
    q = deque([(begin, 0)])
    while q:
        cur, step = q.popleft()
        ch[cur] = 1
        if cur == target:
            return step
        
        for word in words:
            if cur != word and not ch[word]:
                cnt = 0
                for i in range(len(cur)):
                    if cur[i] != word[i]:
                        cnt += 1
                if cnt == 1:
                    q.append((word, step + 1))