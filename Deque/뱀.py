import sys
input=sys.stdin.readline
from collections import deque

n=int(input().rstrip())
board=[[0]*(n+1) for _ in range(n+1)]

for _ in range(int(input().rstrip())):
    r,c=map(int,input().rstrip().split())
    board[r][c]=1
q=deque([])
for _ in range(int(input().rstrip())):
    x,c=input().rstrip().split()
    q.append((int(x),c))

dx=[0,1,0,-1]
dy=[1,0,-1,0]
i=0
time=0
body=deque([(1,1)])
x,y=body[0][0],body[0][1] # 현재 위치

while True:
    nx=x+dx[i]
    ny=y+dy[i]
    # 현재 위치(머리가 위치한 칸)가 유효하지 않는 경우
    # CASE 1: 벽인 경우 (범위 밖)
    if nx<=0 or nx>n or ny<=0 or ny>n:
        break
    # CASE 2: 자기자신의 몸과 부딪히는 경우
    if (nx,ny) in body:
        break
    # 이동할 칸(머리가 위치한 칸)이 유효한 경우
    # CASE 1: 사과가 있는 경우
    if board[nx][ny]==1:
        board[nx][ny]=0
    # CASE 2: 사과가 없는 경우
    else:
        body.popleft()

    x,y=nx,ny
    time+=1
    body.append((nx, ny))

    # 방향 회전
    if q and q[0][0] == time:
        _, c = q.popleft()
        if c == 'L':
            i = (i - 1) % 4
        elif c == 'D':
            i = (i + 1) % 4

print(time+1)
