cnt_zero=0
cnt_one=0

def dfs(arr,sx,sy,n):
    global cnt_zero;global cnt_one
    # 분할된 부분의 첫 원소를 기준점으로 잡음
    flag=arr[sx][sy]
    for i in range(sx,sx+n):
        for j in range(sy,sy+n):
            # 종료 조건 (분할 후 종료)
            if arr[i][j]!=flag:
                dfs(arr,sx,sy,n//2)
                dfs(arr,sx+n//2,sy,n//2)
                dfs(arr,sx,sy+n//2,n//2)
                dfs(arr,sx+n//2,sy+n//2,n//2)
                return
    if flag==0:
        cnt_zero+=1
    else:
        cnt_one+=1
        
def solution(arr):
    n=len(arr[0])
    dfs(arr,0,0,n)
    
    return [cnt_zero,cnt_one]