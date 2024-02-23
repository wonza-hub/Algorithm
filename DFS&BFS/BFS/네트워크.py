from collections import deque

def bfs(x, n, computers, ch):
    q = deque([x])
    while q:
        com = q.popleft()
        ch[com] = 1
        for another_com in range(n):
            if another_com != com and ch[another_com] == 0:
                if computers[com][another_com] == 1:
                    q.append(another_com)

def solution(n, computers):
    answer = 0
    ch = [0] * n
    for i in range(n):
        if not ch[i]:
            bfs(i, n, computers, ch)
            answer += 1

    return answer
