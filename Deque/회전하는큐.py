from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
position = list(map(int, input().split()))
dq = deque([i for i in range(1, n + 1)])

answer = 0
for p in position:
    while True:
        if dq[0] == p:
            dq.popleft()
            break
        else:
            if dq.index(p) < len(dq) / 2:
                while dq[0] != p:
                    dq.append(dq.popleft())
                    answer += 1
            else:
                while dq[0] != p:
                    dq.appendleft(dq.pop())
                    answer += 1
print(answer)