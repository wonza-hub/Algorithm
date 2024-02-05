from collections import deque

def solution(menu, order, k):
    ans = 0
    q = deque()
    complete = -1
    idx = 0
    for t in range((len(order) - 1) * k + 1):
        if t == complete:
            q.popleft()
            complete = -1
        if t % k == 0:
            q.append(order[idx])
            idx += 1
        if complete == -1 and len(q) > 0:
            complete = t + menu[q[0]]
        ans = max(ans, len(q))
        
    return ans
        
    