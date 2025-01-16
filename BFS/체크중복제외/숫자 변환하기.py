# 오답 풀이
from collections import deque

def solution(x, y, n):
    q = deque()
    q.append((x, 0))
    while q:
        x,cnt=q.popleft()
        if x==y:
            return cnt
        if x>y:
            continue
        s=set([x+n,x*2,x*3])
        for ele in s:
            if ele>y:
                continue
            q.append((ele,cnt+1))
        
    return -1
    
from collections import deque

# 정답 풀이
def solution(x, y, n):
    queue = deque()
    queue.append((x,0))
    visited = set() # 포인트
    while queue:
        i, j = queue.popleft()
        if i>y or i in visited:
            continue
        visited.add(i)
        if i==y: 
            return j
        for k in (i*3,i*2,i+n):
            if k<=y and k not in visited:
                queue.append((k,j+1))    
    return -1