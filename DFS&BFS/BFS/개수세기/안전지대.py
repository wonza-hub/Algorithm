def solution(board):
    answer = 0
    
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    
    n = len(board[0])
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for k in range(8):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if board[nx][ny] == 0 and board[nx][ny] != 1:
                            board[nx][ny] = -1
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                answer += 1
    return answer