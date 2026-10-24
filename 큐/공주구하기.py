from collections import deque

n, k = map(int, input().split())
q = deque(list(prince for prince in range(1, n + 1)))
ans = 0
cnt = 0
while q:
    if len(q) == 1:
        ans = q.pop()
        break
    cnt += 1
    tmp = q.popleft()
    if cnt % k == 0:
        continue
    q.append(tmp)

print(ans)