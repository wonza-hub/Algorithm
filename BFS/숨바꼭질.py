from collections import deque
MAX_DIS = 100001

n, k = map(int, input().split())
q = deque()
q.append(n)
ch = [-1] * (MAX_DIS + 1)
ch[n] = 0

while q:
    cur_n = q.popleft()
    if cur_n == k:
        print(ch[cur_n])
        break
    if 0 <= cur_n * 2 < MAX_DIS and ch[cur_n * 2] == -1:
        ch[cur_n * 2] = ch[cur_n] + 1
        q.append(cur_n * 2)
    if 0 <= cur_n + 1 < MAX_DIS and ch[cur_n + 1] == -1:
        ch[cur_n + 1] = ch[cur_n] + 1
        q.append(cur_n + 1)
    if 0 <= cur_n - 1 < MAX_DIS and ch[cur_n - 1] == -1:
        ch[cur_n - 1] = ch[cur_n] + 1
        q.append(cur_n - 1)
