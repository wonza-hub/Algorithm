def is_win(board, mark):
    for row in board:
        if row == [mark, mark, mark]:
            return True
        
    for col in range(3):
        if [board[row][col] for row in range(3)] == [mark, mark, mark]:
            return True
        
    if [board[0][0], board[1][1], board[2][2]] == [mark, mark, mark]:
        return True
    if [board[2][0], board[1][1], board[0][2]] == [mark, mark, mark]:
        return True
    
    return False
    
    
def solution(board):
    board = [list(row) for row in board]
    
    cnt_O, cnt_X = 0, 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                cnt_O += 1
            if board[i][j] == 'X':
                cnt_X += 1
    cnt_diff = cnt_O - cnt_X
                
    if not (cnt_diff == 0 or cnt_diff == 1):
        return 0
    
    if is_win(board, 'O') and is_win(board, 'X'):
        return 0
    
    if is_win(board, 'O') and cnt_diff != 1:
        return 0
    
    if is_win(board, 'X') and cnt_diff != 0:
        return 0
    
    return 1