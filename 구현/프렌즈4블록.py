from collections import deque

def print2d(arr):
    for a in arr:
        print(*a)
        
def is_four_block(board,i,j,m,n):
    if i+1>=m or j+1>=n:
        return False
    if board[i][j]!=0 and board[i][j]==board[i][j+1]==board[i+1][j]==board[i+1][j+1]:
        return True
    return False
        
def solution(m, n, board):
    board=[list(s) for s in board]
    answer = 0
    while True:
        tmp=set()
        for i in range(m):
            for j in range(n):
                if is_four_block(board,i,j,m,n):
                    tmp.add((i,j))
                    tmp.add((i,j+1))
                    tmp.add((i+1,j))
                    tmp.add((i+1,j+1))

        if len(tmp)==0:
            break

        answer+=len(tmp)
        for x,y in tmp:
            board[x][y]=0

        for j in range(n):
            q=deque()
            for i in range(m-1,-1,-1):
                if board[i][j]==0:
                    continue
                q.append(board[i][j])
                board[i][j]=0
            for i in range(m-1,-1,-1):
                if len(q)!=0:
                    ele=q.popleft()
                    board[i][j]=ele
            
    return answer