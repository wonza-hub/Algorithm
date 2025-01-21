n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
cnt_one = 0
cnt_zero = 0
    
def solution(sx, sy, n):
    global cnt_one
    global cnt_zero
    flag = paper[sx][sy]
    for x in range(sx, sx + n):
        for y in range(sy, sy + n):
            if flag != paper[x][y]:
                solution(sx, sy, n // 2)
                solution(sx, sy + n // 2, n // 2)
                solution(sx + n // 2, sy, n // 2)
                solution(sx + n // 2, sy + n // 2, n // 2)
                return
    if flag == 1:
        cnt_one += 1
    else:
        cnt_zero += 1                

solution(0, 0, n)
print(cnt_zero)
print(cnt_one)
    
# 복습 풀이
n=int(input())
paper=[list(map(int,input().split())) for _ in range(n)]
cnt_one=0
cnt_zero=0

def divide(x,y,N): # 시작점의 행 x, 열 y 정보와 한 변의 길이 N
    global cnt_one, cnt_zero
    flag=paper[x][y]
    for i in range(x,x+N):
        for j in range(y,y+N):
            # 이때까지 탐색한 색과 다르면 분할 수행
            if paper[i][j]!=flag:
                divide(x,y,N//2)
                divide(x,y+N//2,N//2)
                divide(x+N//2,y,N//2)
                divide(x+N//2,y+N//2,N//2)
                return
    if flag==1:
        cnt_one+=1
    else:
        cnt_zero+=1

divide(0,0,n)
print(cnt_zero)
print(cnt_one)