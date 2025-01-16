from collections import deque

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def solution(board):
    board=[list(b) for b in board]
    n,m=len(board),len(board[0])
    rx,ry,gx,gy=-1,-1,-1,-1
    cnt=0
    for i in range(n):
        for j in range(m):
            if board[i][j]=='R':
                rx,ry=i,j
            if board[i][j]=='G':
                gx,gy=i,j
    q=deque()
    q.append((rx,ry,cnt))

    while q:
        ox,oy,cnt=q.popleft()
        if ox==gx and oy==gy:
            return cnt
        for i in range(4):
            nx,ny=ox,oy # 초기화 시점 중요!
            while 0<=nx+dx[i]<n and 0<=ny+dy[i]<m and board[nx+dx[i]][ny+dy[i]]!='D':
                nx+=dx[i]
                ny+=dy[i]
            if (nx==ox and ny==oy) or board[nx][ny]=='x':
                continue
            board[nx][ny]='x'
            q.append((nx,ny,cnt+1))
                
    return -1