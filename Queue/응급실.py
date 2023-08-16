from collections import deque

n, m = map(int, input().split())
pats = list(map(int, input().split()))
q = deque((idx, pat) for (idx, pat) in enumerate(pats))
ord = 0

while q:
    tmp = q.popleft()
    if any(tmp[1] < x[1] for x in q):
        q.append(tmp)
    else:
        ord += 1
        if tmp[0] == m:
            break

print(ord)
        