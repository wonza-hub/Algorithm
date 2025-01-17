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

# 복습 풀이
from collections import deque

n,k=map(int,input().split())
MAX_VAL=100001
pos=[0]*MAX_VAL
q=deque([])
q.append(n)
pos[n]=1

while q:
    x=q.popleft()
    if x==k:
        print(pos[x]-1)
        break
    if 0<=x-1<MAX_VAL and pos[x-1]==0:
        pos[x-1]=pos[x]+1
        q.append(x-1)
    if 0<=x+1<MAX_VAL and pos[x+1]==0:
        pos[x+1]=pos[x]+1
        q.append(x+1)
    if 0<=2*x<MAX_VAL and pos[2*x]==0:
        pos[2*x]=pos[x]+1
        q.append(2*x)
    