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
    