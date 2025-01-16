from collections import deque

dx=[-2,-1,-2,-1,1,2,2,1]
dy=[-1,-2,1,2,-2,-1,1,2]

def solution():
    l = int(input())
    board = [[0] * l for _ in range(l)]

    q=deque()
    cur_x,cur_y = map(int, input().split())
    board[cur_x][cur_y]=1
    tar_x,tar_y = map(int, input().split())
    q.append((cur_x,cur_y))

    while q:
        x, y = q.popleft()
        if x == tar_x and y == tar_y:
            ans = board[x][y] - 1
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            # print(nx, ny,)
            if 0<=nx<l and 0<=ny<l and board[nx][ny]==0:
                board[nx][ny]=board[x][y]+1
                q.append((nx,ny))
    return ans

for _ in range(int(input())):
    ans = solution()
    print(ans)