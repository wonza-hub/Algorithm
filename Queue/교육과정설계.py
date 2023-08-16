from collections import deque

ord = input()
n = int(input())
for i in range(1, n + 1):
    q = deque(ord)
    plan = input()
    for sub in plan:
        if sub in q:
            if sub == q[0]:
                q.popleft()
            else:
                ans = 'NO'
                break
        if len(q) == 0:
            ans = 'YES'
            break
    if len(q) != 0:
        ans = 'NO'
    print(f'#{i} {ans}')