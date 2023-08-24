from collections import deque

s, e = map(int, input().split())
check = [0] * 10001
check[s] = 1
list = [0] * 10001
dx = [1, -1, 5]
ans = 0

q = deque([s])

while q:
    now = q.popleft()
    if now == e:
        ans = list[now]
        break
    for i in range(len(dx)):
        next = now + dx[i]
        if 1 <= next <= 10000:
            if check[next] == 1:
                continue
            check[next] = 1
            list[next] = list[now] + 1
            q.append(next)

print(ans)